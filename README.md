# ATM Project

[![Python Tests](https://github.com/DKirdak25/atm-project/actions/workflows/python-tests.yml/badge.svg)](https://github.com/DKirdak25/atm-project/actions/workflows/python-tests.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/)
[![Pytest](https://img.shields.io/badge/testing-pytest-green)](https://pytest.org/)

A simple yet comprehensive ATM (Automated Teller Machine) application built with Python, demonstrating best practices in software architecture, testing, and CI/CD automation.

## 🚀 Features

- 💰 **Deposit money** - Add funds to your account
- 💸 **Withdraw money** - Safely remove funds with overdraft protection
- 📊 **Check balance** - View your current account balance
- ✅ **Input validation** - Robust error handling for user inputs
- 🛡️ **Overdraft protection** - Prevents withdrawing more than available balance
- 🧪 **Automated testing** - Comprehensive test suite with Pytest
- 🎭 **Mocking** - Unit tests with mocked user interactions
- 🔄 **CI/CD** - GitHub Actions workflow for automated testing

## 📁 Project Structure

```
atm-project/
├── atm_logic.py              # Core ATM business logic
├── atm_interface.py          # User interface
├── test_atm.py               # Unit tests
├── README.md                 # This file
└── .github/
    └── workflows/
        └── python-tests.yml  # GitHub Actions CI workflow
```

## 📋 Requirements

- **Python** 3.12 or higher
- **Pytest** (for running tests)

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DKirdak25/atm-project.git
   cd atm-project
   ```

2. **Install dependencies:**
   ```bash
   pip install pytest
   ```

## 🏃 Running the Application

Start the ATM application:

```bash
python atm_interface.py
```

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Or using Python's module syntax:

```bash
python -m pytest
```

### Test Coverage

Our test suite includes:

- ✓ Successful deposits
- ✓ Successful withdrawals
- ✓ Overdraft protection validation
- ✓ Invalid deposit handling
- ✓ Menu input validation
- ✓ Amount input validation
- ✓ Mocked user interactions

## 📚 Concepts Practiced

This project demonstrates proficiency in:

- Object-Oriented Programming (Classes & Objects)
- Functions and modularity
- Separation of Concerns
- Unit Testing & Assertions
- Test-Driven Development (TDD)
- Pytest framework
- Mocking with `unittest.mock`
- Git & Version Control
- GitHub Actions & CI/CD Pipeline

## 🔮 Future Improvements

- [ ] Transaction history tracking
- [ ] Data persistence (file/database storage)
- [ ] Multi-account support
- [ ] PIN/password authentication
- [ ] Enhanced exception handling
- [ ] Logging system
- [ ] Web interface (Flask/Django)

## 🤝 Contributing

Contributions are welcome! Feel free to fork and submit pull requests.

## 📄 License

This project is open source and available under the MIT License.

## ✨ Author

Built as a learning project to practice Python fundamentals, test-driven development, and CI/CD automation.

---

**Last updated:** June 2026
