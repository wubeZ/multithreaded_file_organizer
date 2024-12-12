# Multithreaded File Organizer

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A multithreaded CLI tool to organize files efficiently by type, date, or size. This tool is perfect for decluttering directories and automating file management tasks.

---

## Features
- **Organize by File Type**: Group files into folders based on their extensions (e.g., `.txt`, `.jpg`).
- **Organize by Date**: Sort files into folders by their creation or modification date.
- **Organize by Size**: Categorize files into small, medium, and large based on size thresholds.
- **Dry-Run Mode**: Preview changes without making actual modifications.
- **Multithreaded Processing**: Uses threads to handle file organization faster, especially in large directories.
- **Custom Logging**: Logs all actions to the console or a specified file.

---

## Installation

### Using `pip`:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/multithreaded-file-organizer.git
   cd multithreaded-file-organizer
   ```
2. Install the package:
   ```bash
   pip install .
   ```

---

## Usage

### Basic Command
```bash
organize --path <directory_path> --by <method>
```

### Options
- `--path`: Path to the directory to organize (required).
- `--by`: Organization method. Choose from:
  - `type`: Organize by file type.
  - `date`: Organize by creation/modification date.
  - `size`: Organize by file size.
- `--dry-run`: Simulate changes without making any modifications.
- `--log`: Log actions to a specified file.
- `--recursive`: Organize files in subdirectories as well.

### Examples

1. Organize by file type:
   ```bash
   organize --path ./Downloads --by type
   ```

2. Organize by date with dry-run mode:
   ```bash
   organize --path ./Documents --by date --dry-run
   ```

3. Organize by size and log actions to a file:
   ```bash
   organize --path ./Projects --by size --log organize.log
   ```

---

## How It Works

1. **Categorization**: The tool scans the directory and groups files based on the selected method (type, date, or size).
2. **Multithreading**: Tasks are distributed across multiple threads to optimize performance.
3. **Action Execution**: Moves files to their respective folders. If `--dry-run` is enabled, no changes are made.
4. **Logging**: Logs each action to the console or a file for review.

---

## Development

### Running Tests
1. Install `pytest`:
   ```bash
   pip install pytest
   ```
2. Run the test suite:
   ```bash
   pytest tests/
   ```

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by the need for efficient file organization.
- Thanks to the Python community for making great tools like `argparse` and `concurrent.futures` available.

---

Happy organizing! 🎉
