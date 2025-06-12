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
mkdir -p docs/{en,zh}/{getting-started,specializations,resources}

# Set up i18n structure
echo "Setting up multilingual structure..."
chmod +x setup_i18n.sh
./setup_i18n.sh

echo "Setup complete! To start the development server:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the development server: mkdocs serve"
echo ""
echo "The site will be available at http://127.0.0.1:8000"
echo "Language versions will be at:"
echo "- English: http://127.0.0.1:8000/en/"
echo "- Chinese: http://127.0.0.1:8000/zh/" 