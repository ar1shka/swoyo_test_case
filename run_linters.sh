#!/bin/bash

echo "[1] Run black..."
poetry run black . --config=./pyproject.toml

echo "[2] Run isort..."
poetry run isort . --settings-file=./pyproject.toml

echo "[3] Run flake8..."
poetry run flake8 . --config=./.flake8

echo "[4] Run mypy..."
poetry run mypy . --config-file=./mypy.ini