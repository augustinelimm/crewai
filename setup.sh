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

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << EOF
OPENAI_API_KEY=your_openai_api_key_here
EOF
    echo "Please edit .env file with your actual OpenAI API key"
fi

echo "Setup complete! Run: poetry run python main.py"