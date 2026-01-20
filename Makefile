.PHONY: help install run test migrate seed clean docker-up docker-down

help:
	@echo "izone-workforce API - Available Commands"
	@echo "========================================"
	@echo "make install     - Install dependencies"
	@echo "make run         - Run the development server"
	@echo "make test        - Run tests"
	@echo "make migrate     - Run database migrations"
	@echo "make seed        - Seed database with initial data"
	@echo "make clean       - Clean up cache and temp files"
	@echo "make docker-up   - Start Docker containers"
	@echo "make docker-down - Stop Docker containers"

install:
	pip install -r requirements.txt

run:
	python run.py

test:
	pytest tests/ -v

migrate:
	alembic upgrade head

seed:
	python seed_data.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f api
