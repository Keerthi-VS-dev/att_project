from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models.employee import Employee, UserRole
from app.utils.security import decode_token
from app.schemas.employee import TokenData

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> Employee:
    """Get the current authenticated user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = decode_token(token)
        employee_id: int = payload.get("sub")
        
        if employee_id is None:
            raise credentials_exception
            
        token_data = TokenData(employee_id=employee_id)
    except Exception:
        raise credentials_exception
    
    employee = db.query(Employee).filter(Employee.employee_id == token_data.employee_id).first()
    
    if employee is None:
        raise credentials_exception
    
    if not employee.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    
    return employee


def get_current_active_user(
    current_user: Employee = Depends(get_current_user)
) -> Employee:
    """Get current active user"""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    return current_user


def require_role(required_roles: list[UserRole]):
    """Dependency to check if user has required role"""
    def role_checker(current_user: Employee = Depends(get_current_user)) -> Employee:
        if current_user.role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        return current_user
    return role_checker


def get_current_admin(
    current_user: Employee = Depends(get_current_user)
) -> Employee:
    """Get current user if they are an admin"""
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user


def get_current_manager_or_admin(
    current_user: Employee = Depends(get_current_user)
) -> Employee:
    """Get current user if they are a manager or admin"""
    if current_user.role not in [UserRole.ADMIN, UserRole.MANAGER]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Manager or Admin access required"
        )
    return current_user
