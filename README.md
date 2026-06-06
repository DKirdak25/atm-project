ATM Project

A simple ATM application built with Python using separation of business logic and user interface.

Features

- Deposit money
- Withdraw money
- Check account balance
- Input validation
- Prevents overdrawing
- Automated testing with Pytest
- Mocking for user input testing

Project Structure

Automation_Project/
│
├── atm_logic.py
├── atm_interface.py
├── test_atm.py
├── README.md
└── .github/
    └── workflows/
        └── python-tests.yml

Requirements

- Python 3.12+
- Pytest

Installation

Clone the repository:

git clone <repository-url>
cd atm-project

Install Pytest:

pip install pytest

Running the Application

python atm_interface.py

Running Tests

pytest

or

python -m pytest

Test Coverage

The test suite covers:

- Successful deposits
- Successful withdrawals
- Over-withdraw protection
- Invalid deposits
- User menu input validation
- Amount input validation
- Mocked user interaction

Concepts Practiced

- Functions
- Classes and Objects
- Separation of Concerns
- Assertions
- Unit Testing
- Pytest
- Mocking with unittest.mock
- Git
- GitHub Actions (CI)

Future Improvements

- Transaction history
- Data persistence using files or a database
- Multiple accounts
- PIN authentication
- Exception handling improvements

Author

Built as a learning project to practice Python fundamentals, testing, and CI/CD.
