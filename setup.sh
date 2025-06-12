#!/bin/bash

# Create and activate virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Initialize MkDocs
echo "Setting up MkDocs..."
mkdir -p docs/{getting-started,specializations,resources}

# Create necessary directories for content
echo "Creating content directories..."
for dir in docs/getting-started docs/specializations docs/resources; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
    fi
done

echo "Setup complete! To start the development server:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the development server: mkdocs serve" 