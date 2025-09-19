#!/usr/bin/env python3
"""
Simple wrapper to update MkDocs navigation and translations.
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

# Import the main function from update_mkdocs
from update_mkdocs import main as update_mkdocs_main

def main():
    """Update MkDocs navigation and translations."""
    update_mkdocs_main()

if __name__ == "__main__":
    main()
