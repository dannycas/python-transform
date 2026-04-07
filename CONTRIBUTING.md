# Contributing

Thank you for your interest in contributing to the python-transform project!

## How can you help?

### Reporting bugs

If you found a bug, open an issue with:
- Problem description
- Steps to reproduce
- Expected behavior
- Actual behavior
- System information (OS, Python version, etc.)

### Feature suggestions

If you have an idea for a new feature:
- Open an issue with the title: `[FEATURE REQUEST]`
- Describe the problem it would solve
- Propose a solution (optional)

### Preparing Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/python-transform.git
   ```

2. **Create a branch for your feature/fix**
   ```bash
   git checkout -b feature/my-new-feature
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   pip install pytest flake8
   ```

4. **Make your changes**
   - Write readable code
   - Add docstrings
   - Maintain the existing code style

5. **Run tests**
   ```bash
   python -m pytest tests/
   ```

6. **Check code quality**
   ```bash
   flake8 --max-line-length=120 .
   ```

7. **Commit your changes**
   ```bash
   git commit -am 'Add my new feature'
   ```

8. **Push to your branch**
   ```bash
   git push origin feature/my-new-feature
   ```

9. **Open a Pull Request**
   - Describe what you changed
   - Link related issues

## Coding standards

- PEP 8 compliance (max 120 characters per line)
- Docstrings for all functions/classes
- Type hints where possible
- Tests for new functionality

## Review process

All PRs will be reviewed before acceptance:
- Code review
- Tests
- Documentation
- Standards compliance

## Questions?

Open an issue or contact the maintainers.

Thank you for your contribution! 🎉
