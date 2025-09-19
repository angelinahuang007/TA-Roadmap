#!/usr/bin/env python3
"""
Update mkdocs.yml navigation and i18n translations based on docs folder structure.

This script scans the docs folder and automatically updates the navigation
structure in mkdocs.yml and maintains i18n translations in .i18n/en.yml.
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Any

# Constants
DOCS_PATH = "docs"
MKDOCS_YML_PATH = "mkdocs.yml"
I18N_PATH = ".i18n/en.yml"
translations = {} # {english: chinese}

# load tranlate file and assign to translations
def load_translations(path: str) -> None:
    # need global here becuase assigning translations 
    global translations
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)
            if content and 'nav' in content:
                translations = content['nav']
    except yaml.YAMLError as e:
        print(f"Error parsing {path}: {e}")
        exit(1)

def translate(key: str) -> str:
    if key in translations:
        return translations[key]
    return key

def parse_prefix(name: str):
    """Return (prefix, clean_name) if name starts with digits_ else None."""
    import re
    m = re.match(r'^(\d+)_+(.+)', name)
    if not m:
        return None
    return int(m.group(1)), m.group(2)

def build_nav(path: Path) -> List[Dict[str, Any]]:
    """Build navigation recursively for any path."""
    items = []
    entries = []

    # Folders
    for p in path.iterdir():
        if p.is_dir() and not p.name.startswith('.') and p.name not in {'assets', 'javascripts'}:
            parsed = parse_prefix(p.name)
            if parsed:
                prefix, clean = parsed
                entries.append((prefix, 'folder', p, clean))

    # Files
    for p in path.glob('*.md'):
        if not p.name.endswith('.en.md'):
            parsed = parse_prefix(p.stem)
            if parsed:
                prefix, clean = parsed
                entries.append((prefix, 'file', p, clean))

    # Sort by prefix
    entries.sort(key=lambda x: x[0])

    for _, kind, p, clean in entries:
        if kind == 'file':
            items.append({clean: str(p.relative_to(Path(DOCS_PATH))).replace("\\", "/")})
        else:
            sub = build_nav(p)
            if sub:
                items.append({clean: sub})
            else:
                # Fall back to first file if no children
                first_file = next(p.glob("*.md"), None)
                if first_file and not first_file.name.endswith('.en.md'):
                    items.append({clean: str(first_file.relative_to(Path(DOCS_PATH))).replace("\\", "/")})
    
    return items

def generate_navigation() -> List[Dict[str, Any]]:
    """Generate the complete navigation structure."""
    docs = Path(DOCS_PATH)
    nav = []
    if (docs / "index.md").exists():
        nav.append({"Home": "index.md"})
    nav.extend(build_nav(docs))
    return nav

def update_mkdocs_config():
    """Update the mkdocs.yml file with new navigation structure and nav_translations."""
    try:
        with open(MKDOCS_YML_PATH, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error parsing {MKDOCS_YML_PATH}: {e}")
        exit(1)
    
    # Generate new navigation
    new_nav = generate_navigation()
    
    # Update navigation
    config['nav'] = new_nav
    
    # Update nav_translations in i18n plugin configuration
    for plugin in config.get('plugins', []):
        if isinstance(plugin, dict) and 'i18n' in plugin:
            for lang in plugin['i18n'].get('languages', []):
                if lang.get('locale') == 'zh':
                    lang['nav_translations'] = translations
    
    # Write updated config
    try:
        with open(MKDOCS_YML_PATH, 'w', encoding='utf-8') as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True, 
                     sort_keys=False, width=1000)
        print(f"Updated {MKDOCS_YML_PATH} with new navigation structure.")
    except Exception as e:
        print(f"Error writing {MKDOCS_YML_PATH}: {e}")
        exit(1)

def main():
    """Main function to update mkdocs navigation and translations."""
    print("Updating MkDocs navigation and i18n translations...")
    
    # Check all required files exist
    if not Path(DOCS_PATH).exists() or not Path(MKDOCS_YML_PATH).exists() or not Path(I18N_PATH).exists():
        print(f"File not found")
        exit(1)
    
    # Load translations for nav_translations
    load_translations(I18N_PATH)
    
    # Update files
    update_mkdocs_config()
    
    print("✅ MkDocs navigation and translations updated successfully!")

if __name__ == "__main__":
    main()