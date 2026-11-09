
# QUANTUM-X QA Automation Framework

[![QUANTUM-X Playwright Tests](https://github.com/Visvesh19/quantum-x-qa-automation/actions/workflows/playwright-tests.yml/badge.svg?branch=main)](https://github.com/Visvesh19/quantum-x-qa-automation/actions/workflows/playwright-tests.yml)

**Python | Playwright | pytest | Page Object Model | GitHub Actions**

A web UI automation framework demonstrating functional, negative,
data-driven, and end-to-end testing using Python and Playwright.

**Application Under Test:** [SauceDemo](https://www.saucedemo.com/)

## Project Highlights

- 14 automated test cases
- Page Object Model (POM) architecture
- Positive and negative functional testing
- Data-driven test execution with pytest
- End-to-end checkout automation
- Cross-page product price consistency validation
- Subtotal, tax, and grand total verification using Decimal
- Screenshots captured on test failure
- HTML test execution reports
- Automated CI execution using GitHub Actions

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Test automation programming |
| Playwright | Browser automation |
| pytest | Test execution and assertions |
| pytest-playwright | Browser fixtures and integration |
| pytest-html | HTML test reporting |
| GitHub Actions | Continuous integration |
| Git | Version control |

## Framework Architecture

```text
QUANTUM-X/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_login_data_driven.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_checkout_negative.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Coverage

| Module | Validations |
|--------|-------------|
| Login | Successful and unsuccessful authentication |
| Data-driven Login | Invalid credentials and mandatory fields |
| Inventory | Product listing and add-to-cart |
| Cart | Product details and quantity |
| Checkout | End-to-end order completion |
| Price Consistency | Inventory vs Cart vs Checkout |
| Financial Validation | Subtotal, 8% tax, and total |
| Negative Checkout | Required first name, last name, and postal code |

## Running Tests Locally

### 1. Clone the repository

```bash
git clone https://github.com/Visvesh19/quantum-x-qa-automation.git
cd quantum-x-qa-automation
```

Note: This repository may require GitHub authentication
while it remains private.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install Chromium

```bash
python -m playwright install chromium
```

### 5. Execute all tests

```bash
python -m pytest
```

### 6. Generate an HTML report

```bash
python -m pytest --html=report.html --self-contained-html
```

Open `report.html` in a browser to review the results.

## Continuous Integration

GitHub Actions automatically executes the test suite
when code is pushed to the main branch or a pull request
targets main.

The CI workflow:

1. Checks out the repository
2. Configures Python 3.13
3. Installs pinned Python dependencies
4. Installs Chromium and required system libraries
5. Executes the automated regression suite
6. Generates an HTML test report
7. Uploads execution artifacts

[View GitHub Actions Runs](https://github.com/Visvesh19/quantum-x-qa-automation/actions)

## Execution Results

Latest verified local regression:

- Tests executed: 14
- Passed: 14
- Failed: 0
- Execution time: 18.74 seconds
- Browser: Chromium

GitHub Actions workflow run #2 completed successfully
in 40 seconds and uploaded one report artifact.

Execution results may change as the application,
dependencies, and test suite evolve.

## Automation Design

### Page Object Model

Page classes encapsulate locators and reusable browser
interactions, separating UI implementation from test logic.

### Data-Driven Testing

pytest parameterization is used to execute multiple
test scenarios with different input combinations.

### Financial Validation

Python Decimal provides precise monetary comparisons
for product prices, subtotal, tax, and order total.

### Failure Evidence

Playwright is configured to capture screenshots when
tests fail.

## Future Enhancements

- Additional inventory and cart scenarios
- Cross-browser testing
- Improved test data management
- Expanded negative and boundary testing
- CI execution improvements
- Additional real-world automation projects

## Author

**Visveswaran**

Associate Project Manager | Software Testing | QA Automation

[GitHub Profile](https://github.com/Visvesh19)
