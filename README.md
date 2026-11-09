
# QUANTUM-X QA Automation Framework

A Python-based web UI test automation framework built using
Playwright, pytest, and the Page Object Model (POM).

## Project Overview

QUANTUM-X demonstrates practical test automation skills through
functional, negative, data-driven, and end-to-end testing.

Application under test:
https://www.saucedemo.com/

## Technology Stack

- Python
- Playwright
- pytest
- pytest-playwright
- pytest-html
- Git and GitHub

## Framework Architecture

```text
QUANTUM-X/
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

| Module | Test Coverage |
|--------|---------------|
| Login | Valid and invalid authentication |
| Data-driven Login | Multiple negative login scenarios |
| Inventory | Product listing and add-to-cart |
| Cart | Product details and quantity |
| Checkout | Complete end-to-end purchase |
| Price Validation | Inventory, cart, checkout consistency |
| Financial Validation | Subtotal, tax and grand total |
| Negative Checkout | Mandatory customer information |

## Current Execution Results

- Total automated tests: 14
- Latest regression result: 14 passed
- Execution time: 18.74 seconds
- Browser: Chromium

These results represent a local execution snapshot,
not a guarantee of future execution success.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Visvesh19/quantum-x-qa-automation.git
cd quantum-x-qa-automation
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install Playwright browser

```bash
python -m playwright install chromium
```

### 5. Run all tests

```bash
python -m pytest
```

### 6. Generate an HTML report

```bash
python -m pytest --html=report.html --self-contained-html
```

Open `report.html` in your browser to review the results.

## Framework Design

### Page Object Model

UI locators and reusable actions are maintained in page classes,
keeping test scenarios separate from implementation details.

### Data-Driven Testing

pytest parameterization allows multiple input combinations
to be tested through reusable test functions.

### Financial Assertions

Python Decimal is used to validate monetary values and
reduce floating-point rounding issues.

### Failure Evidence

Playwright captures screenshots on test failure.

## Planned Enhancements

- GitHub Actions CI pipeline
- Multi-browser execution
- Additional negative scenarios
- Test data management
- Improved reporting and execution evidence

## Author

Visveswaran

QA Automation | Software Testing | Test Management

GitHub: https://github.com/Visvesh19
