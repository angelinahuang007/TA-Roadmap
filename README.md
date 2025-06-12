# Technical Artist Roadmap 🎨🔧

A comprehensive guide and resource collection for aspiring Technical Artists in the game industry. This roadmap covers various specializations, essential skills, and curated learning resources for each path.

## Development Setup

### Prerequisites

- Windows Subsystem for Linux (WSL2)
- Python 3.8 or higher
- Git

### Setting Up WSL

1. Open PowerShell as Administrator and run:
```powershell
wsl --install
```

2. Restart your computer and complete the Ubuntu setup.

### Setting Up the Development Environment

1. Clone the repository:
```bash
git clone https://github.com/yourusername/TA-Roadmap.git
cd TA-Roadmap
```

2. Run the setup script:
```bash
chmod +x setup.sh
./setup.sh
```

3. Activate the virtual environment:
```bash
source venv/bin/activate
```

4. Start the development server:
```bash
mkdocs serve
```

5. Open your browser and navigate to `http://127.0.0.1:8000`

## Project Structure

```
TA-Roadmap/
├── docs/                    # Documentation source files
│   ├── getting-started/     # Introduction and core skills
│   ├── specializations/     # Different TA paths
│   ├── resources/          # Additional resources
│   └── index.md            # Home page
├── mkdocs.yml              # MkDocs configuration
├── requirements.txt        # Python dependencies
├── setup.sh               # Setup script
└── README.md              # This file
```

## Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

Please read our [Contributing Guide](docs/contributing.md) for more details.

## Building the Documentation

To build the static site:

```bash
mkdocs build
```

The built site will be in the `site` directory.

## Deployment

The documentation is automatically deployed using GitHub Pages when changes are pushed to the main branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- All contributors to this roadmap
- The technical art community
- Game development studios sharing their knowledge
- Open source tools and resources

---

*This roadmap is a living document and will be continuously updated with new resources and information.*
