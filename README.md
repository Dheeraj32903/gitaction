# Python Unit Testing with GitHub Actions

[![Python Unit Tests](https://github.com/Dheeraj32903/gitaction/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Dheeraj32903/gitaction/actions/workflows/python-tests.yml)

A clean and simple Python project demonstrating automated CI (Continuous Integration) using **GitHub Actions**. Whenever code is pushed to this repository, GitHub Actions automatically executes the unit tests and reports the results.

---

## 📁 Project Structure

```text
├── .github/
│   └── workflows/
│       └── python-tests.yml    # GitHub Actions CI workflow
├── src/
│   ├── __init__.py
│   └── calculator.py           # Calculator logic functions
├── tests/
│   ├── __init__.py
│   └── test_calculator.py      # Unit tests using Python's unittest
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧪 Running Tests Locally

You can run the tests locally with verbose output:

```bash
python -m unittest discover -s tests -v
```

Expected output:
```text
test_add (test_calculator.TestCalculator.test_add) ... ok
test_divide (test_calculator.TestCalculator.test_divide) ... ok
test_divide_by_zero (test_calculator.TestCalculator.test_divide_by_zero) ... ok
test_is_even (test_calculator.TestCalculator.test_is_even) ... ok
test_multiply (test_calculator.TestCalculator.test_multiply) ... ok
test_power (test_calculator.TestCalculator.test_power) ... ok
test_subtract (test_calculator.TestCalculator.test_subtract) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

---

## 🚀 How GitHub Actions CI Works

1. **Trigger on Push**: Every time code is pushed or a pull request is made, `.github/workflows/python-tests.yml` triggers automatically.
2. **Setup Runner**: Spawns an `ubuntu-latest` virtual environment and sets up Python 3.11.
3. **Run Tests**: Executes `python -m unittest discover -s tests -v`.
4. **View Execution**:
   - Go to your GitHub repository: [https://github.com/Dheeraj32903/gitaction](https://github.com/Dheeraj32903/gitaction)
   - Click on the **Actions** tab at the top.
   - Click on the latest workflow run (e.g. `Python Unit Tests`).
   - Click on **Run Unit Tests** to see live step-by-step logs and passing test results!
