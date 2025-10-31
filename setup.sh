#!/bin/bash
echo "Setting up Trip Planner Crew..."

# Install Poetry if not installed
if ! command -v poetry &> /dev/null; then
    echo "Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

# Install dependencies
echo "Installing dependencies..."
poetry install

echo "Please add .env file with your actual OPENAI_API_KEY and SERPER_API_KEY"

echo "Setup complete! Run: poetry run python main.py"