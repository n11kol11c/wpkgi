<div align="center">
    <h1>Windows Package Installer</h1>
</div>

<div align="center">
    <p>A powerful, user-friendly Windows package installer built with Python. This tool simplifies the process of installing, managing, and deploying software packages on Windows systems.</p>
</div>

## 🚀 Features

- **Simple Installation**: Install packages with a single command
- **Package Management**: Easily update, remove, or list installed packages
- **Dependency Resolution**: Automatically handles package dependencies
- **Silent Installation**: Support for unattended/silent installations
- **Custom Installation Paths**: Specify where packages should be installed
- **Rollback Support**: Revert to previous states if installations fail
- **Logging**: Comprehensive logging for troubleshooting
- **CLI Interfaces**: Use command-line interfaces

## 📋 Requirements

- Python 3.6 or higher
- Windows 7/8/10/11
- Administrator privileges (for system-wide installations)

## 🔧 Installation

```bash
# Clone the repository
git clone --depth=1 https://github.com/tkemza/wpkgi.git 

# Or clone with 
git clone https://github.com/tkemza/wpkgi.git 

# Navigate to the project directorys bin
cd wpkgi/bin

# Install required dependencies
pip install -r requirements.txt
```

## 📚 Documentation
For complete documentation, visit our manifest: [MANIFEST.in](bin/MANIFEST.in)

## 🔄 How It Works

1. Package Discovery: The installer searches for available packages in configured repositories

2. Dependency Analysis: Identifies and resolves all required dependencies

3. Download: Securely downloads package files from verified sources

4. Verification: Validates package integrity through checksum verification

5. Installation: Executes the installation process with appropriate permissions

6. Registration: Registers the package in the system database for future management

## 🛠️ Development

Project Structure

```ini
wpkgi/
│── app/                  # Main application directory
│   ├── app.bat           # Batch script for running the app
│
├── assets/               # Stores assets like images, logos, and metadata
│   ├── info.py           # Contains metadata or app information
│   ├── main_logo.py      # Possibly for displaying the app logo
│   ├── menu.py           # Manages menu-related functions
│
├── bin/                  # Binary files or scripts
│   ├── MANIFEST.in       # Packaging manifest file
│   ├── requirements.txt  # Dependencies list
│
├── classes/              # Contains various Python classes
│   ├── FileEvent.py      # Handles file-related events
│   ├── OnLoad.py         # Manages on-load events
│   ├── SyntaxError.py    # Custom syntax error handling
│
├── core/                 # Core functionalities of the project
│   ├── __init__.py       # Initializes the core module
│   ├── config.py         # Configuration file
│   ├── packages.json     # Stores package-related data
│
├── docs/                 # Documentation directory
│   ├── README.md         # Project documentation
│
├── handlers/             # Error and event handlers
│   ├── error_handle.py   # Manages error handling
│
├── .gitignore            # Git ignore file
├── config.json           # JSON configuration file
├── LICENSE               # License file
├── README.md             # Main project README
├── wpkgi.py              # Main entry script
```

## 🪟 Preview
<div align="center">
    <img src="" alt="image" hspace="5" vspace="5">
</div>

## 🔒 Security
All package downloads use HTTPS
Packages are verified using SHA-256 checksums
The installer runs with minimal required permissions

## 📝 License
This project is licensed under the GPL-3.0 License - see the LICENSE file for details.

## 👥 Authors
Tkemza - wpkgi - https://github.com/tkemza

## 🙏 Acknowledgments
Python community for excellent libraries

## 📞 Support
For support, please open an issue on the GitHub repository or contact the maintainers directly at tkemaz.git@proton.me or on discord [@n11kol1c](https://discord.com).
