# Automated MkDocs Navigation CI System

This repository includes an automated CI system that generates the `mkdocs.yml` navigation structure based on the folder structure in the `docs` directory.

## How It Works

The system consists of several components:

### 1. Translation File (`.i18n/en.yml`)
This file contains the mapping between Chinese navigation items and their English translations. It serves as the source of truth for all navigation titles and translations in the i18n system.

### 2. Update Script (`scripts/update_mkdocs.py`)
The main Python script that:
- Scans the `docs` folder structure
- Reads translation mappings from `.i18n/en.yml`
- Updates the navigation structure in `mkdocs.yml`
- Preserves existing configurations in `mkdocs.yml`
- Updates `.i18n/en.yml` with any new translations discovered

### 3. GitHub Action (`.github/workflows/update-mkdocs.yml`)
Automated workflow that:
- Triggers on changes to the `docs` folder
- Runs the update script
- Commits changes locally (no automatic push)
- Allows manual review before pushing

### 4. Local Wrapper (`update_navigation.py`)
A simple wrapper script for easy local development and testing.

## Folder Structure Rules

The system uses **numeric prefixes** for automatic ordering:

### Prefix-Based Organization (Strict Requirements)
- **Two-digit prefixes** (01_, 02_, etc.) for top-level folders - **REQUIRED**
- **Three-digit prefixes** (001_, 002_, etc.) for second-level folders - **REQUIRED**  
- **Four-digit prefixes** (0001_, 0002_, etc.) for third-level folders - **REQUIRED**
- **Any numeric prefix** for files at any level
- **Prefixes are hidden** in navigation display
- **Automatic sorting** by prefix number
- **Folders/files without proper prefixes are IGNORED** (except index.md/index.en.md)

### Example Structure
```
docs/
├── index.md                           # 首页 (Home) - always first
├── 01_getting-started/               # Getting Started
│   ├── 001_introduction.md
│   └── 002_setup.md
├── 02_core-skills/                   # 核心技能 (Core Skills)  
│   ├── 001_fundamentals.md
│   ├── 010_computer-science/         # 计算机基础
│   │   ├── 001_mathematics.md        # 数学基础
│   │   ├── 002_data-structures.md    # 数据结构
│   │   ├── 003_algorithms/           # 算法 (folder with multiple files)
│   │   │   ├── 0001_sorting.md       # 排序算法
│   │   │   └── 0002_searching.md     # 搜索算法
│   │   └── 004_programming-languages.md
│   └── 020_art-fundamentals/         # 艺术基础
│       ├── 001_color-theory.md       # 配色理论
│       ├── 002_composition/          # 构图原理 (folder with multiple files)
│       │   ├── 0001_rule-of-thirds.md
│       │   └── 0002_golden-ratio.md
│       └── 003_visual-elements.md
├── 03_specializations/               # 专业方向 (Specializations)
│   ├── 001_procedural-generation/    # 程序化生成
│   ├── 002_shaders-graphics/         # 着色器和图形
│   └── 003_animation/                # 动画技术
├── 04_resources/                     # 资源推荐 (Resources)
└── 05_interview-prep/                # 面试准备

.i18n/
└── en.yml                            # English translations for navigation
```

### File Naming Conventions
- **Use numeric prefixes** for ordering (01_, 02_, 001_, 002_, etc.)
- **Use English names** after the prefix (clean names without prefixes)
- **Chinese translations** are handled via `.i18n/en.yml`
- **Prefixes are stripped** from display names automatically
- `.en.md` files are automatically handled by the i18n plugin
- `index.md` files serve as section introductions

### Prefix Guidelines (Strict Enforcement)
- **Top-level folders**: MUST use exactly 2-digit prefixes (01_, 02_, 03_...)
- **Second-level folders**: MUST use exactly 3-digit prefixes (001_, 002_, 010_, 020_...)
- **Third-level folders**: MUST use exactly 4-digit prefixes (0001_, 0002_, 0010_...)
- **Files**: Can use any numeric prefix for ordering at any level
- **Multiple files**: Each folder can contain multiple prefixed files and subfolders
- **No prefix**: Items without proper prefixes are COMPLETELY IGNORED
- **Exceptions**: Only index.md and index.en.md are processed without prefixes

### i18n Translation System
The system uses the official `mkdocs-static-i18n` translation folder mechanism:
- Navigation translations are stored in `.i18n/en.yml`
- The old `nav_translations` configuration in `mkdocs.yml` is no longer supported
- Translations are automatically managed through the `.i18n/en.yml` file
- The system preserves existing translations and adds new ones as needed

## Usage

### Local Development
To update the navigation locally:
```bash
python3 update_navigation.py
```

Or run the main script directly:
```bash
python3 scripts/update_mkdocs.py --docs docs --config mkdocs.yml
```

### Adding New Content
1. Create folders and files using English names
2. Add translations to `.i18n/en.yml` if needed
3. The CI will automatically update `mkdocs.yml` and preserve/add translations

### Customizing Translations
Edit `.i18n/en.yml` to add or modify translations:

```yaml
# English translations for navigation
nav:
  新章节: New Section
  新主题: New Topic
  新文件标题: New File Title
```

## CI Behavior

### Automatic Updates
- Triggers on pushes to `main`/`master` branch
- Only runs when files in `docs/` are modified
- Automatically commits updated `mkdocs.yml`
- Uses `[skip ci]` to avoid infinite loops

### Pull Request Handling
- For PRs, creates a new PR with navigation updates
- Allows review before merging navigation changes
- Automatically cleans up temporary branches

### Manual Triggering
The workflow can be manually triggered from the GitHub Actions tab.

## Troubleshooting

### Common Issues
1. **Missing translations**: Add entries to `.i18n/en.yml`
2. **Incorrect structure**: Ensure folders follow the two-level rule
3. **File not found**: Check file paths and extensions

### Testing Locally
Before pushing changes, test the navigation generation:
```bash
# Test the script
python3 update_navigation.py

# Check the generated navigation
head -n 50 mkdocs.yml | tail -n 20
```

### Debugging
The script provides verbose output showing:
- Detected folder structure
- Translation mappings used
- Generated navigation items

## Contributing

When adding new sections:
1. Use descriptive English folder names
2. Add appropriate translations to `.i18n/en.yml` if needed
3. Test locally before pushing
4. Follow the existing folder structure patterns

The CI system is designed to be maintenance-free once set up, automatically adapting to changes in the documentation structure.
