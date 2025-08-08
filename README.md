# Pytest Selenium Page Object Model Project Structure
```
greencity_selenium/
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   └── test_product_search.py
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── components/
│   │   ├── __init__.py
│   │   └── header_component.py
│   └── locators/
│       ├── __init__.py
│       ├── login_page_locators.py
│       └── home_page_locators.py
│
├── fixtures/
│   └── conftest.py
│
├── utils/
│   └── helpers.py
│
├── config/
│   └── settings.ini
│
├── requirements.txt
└── README.md
```

# Explanation of Key Elements
## `greencity_selenium/` 🏙️

This is the root folder of your project.

## `tests/` 🧪

Purpose: This directory contains all your test files. Pytest automatically discovers files and functions that start with `test_`.

Example: `test_login.py` contains tests that verify the login functionality, while `test_product_search.py` contains tests for product search.

## `pages/` 📄

Purpose: This is the core of the Page Object Model pattern. Each file in this directory represents a separate web page or component. This structure is now divided into smaller parts for better organization:

### `locators/`: 
Contains all the element locators (ID, XPath, CSS selectors) for different pages. This allows you to centralize and easily update locators. For example, `login_page_locators.py` would only contain selectors for the login page.

### `components/`: 
Contains objects for reusable elements that may appear on multiple pages, such as a site header (`header_component.py`) or footer. This helps avoid code duplication.

`base_page.py`: Typically contains common methods used across all pages (e.g., `find_element(`), `wait_for_element()`).

## fixtures/conftest.py 🔧

Purpose: This is a special Pytest file that allows you to share fixtures (setup and teardown functions) across all tests. This is typically where you initialize and close the Selenium WebDriver.

Example: You can define a browser() fixture that creates a WebDriver instance and passes it to every test that needs it, which helps avoid code duplication.

## utils/ ⚙️

Purpose: This directory is for useful helper functions that don't belong in either the test files or the page objects.

Example: Functions for file handling, generating random data, or taking screenshots.

## `config/` 📋

Purpose: Contains configuration files, such as settings.ini or config.json. This is used to store parameters that may change between environments (e.g., website URL, login credentials, browser settings).

## `requirements.txt` 📦

Purpose: A list of all project dependencies (e.g., pytest, selenium). It's used to install all necessary libraries with a single command: pip install -r requirements.txt.

