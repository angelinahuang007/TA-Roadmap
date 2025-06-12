#!/bin/bash

# Create base directories for each language
mkdir -p docs/{en,zh}/{getting-started,specializations,resources}

# Move existing English content to en directory
mv docs/index.md docs/en/
mv docs/getting-started/* docs/en/getting-started/ 2>/dev/null
mv docs/specializations/* docs/en/specializations/ 2>/dev/null
mv docs/resources/* docs/en/resources/ 2>/dev/null
mv docs/contributing.md docs/en/

# Move Chinese content to zh directory
mv docs/index.zh.md docs/zh/index.md 2>/dev/null

# Create necessary empty files for Chinese translations
touch docs/zh/getting-started/{introduction,core-skills}.md
touch docs/zh/specializations/{pipeline,shaders-and-graphics,animation,vfx,tools}.md
touch docs/zh/resources/{learning-path,community,tools-software}.md
touch docs/zh/contributing.md

echo "Directory structure created successfully!" 