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

echo "Please edit .env file with your actual OpenAI API key"
echo "Setup complete! Run: poetry run python main.py"