Python Unit Testing Lab

This project demonstrates basic unit testing in Python using pytest and continuous integration with GitHub Actions.

Project Structure

Lab/
├── example1.py
├── example2.py
├── test_1.py
└── test_2.py


Features

- Unit testing using pytest
- Automated testing using GitHub Actions
- Test cases included for:
  - Even number checking
  - String reversing


Running Tests Locally

Install pytest:
pip install pytest

Run tests:
pytest


CI/CD

This project uses GitHub Actions to automatically run tests whenever code is pushed to the repository.

The workflow file is located at:
.github/workflows/python-app.yml

All tests must pass before changes are accepted.


Author

Name: Tanmay Arora
Course: Week 5 – Advanced Unit Testing Lab
