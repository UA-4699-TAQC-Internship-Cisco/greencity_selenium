# GreenCity Selenium Test Automation Framework

A comprehensive Selenium-based test automation framework for the GreenCity application using the Page Object Model (POM) pattern with Python and Pytest.

## 🏗️ Project Structure

```
greencity_selenium/
├── tests/                      # Test files (pytest auto-discovers test_*.py)
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_create_news_page.py
│   └── ...
│
├── pages/                      # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py           # Base page functionality
│   ├── base_component.py      # Base component functionality
│   ├── eco_news_list_page.py  # Eco news page objects
│   ├── header_component.py    # Header component
│   └── ...
│
├── fixtures/                   # Pytest fixtures for setup/teardown
│   ├── __init__.py
│   ├── drivers.py             # WebDriver fixtures
│   └── news_page_fixtures.py  # Page-specific fixtures
│
├── config/                     # Configuration and constants
│   ├── __init__.py
│   └── resources.py           # Application URLs, test data, etc.
│
├── api/                        # API utilities (if needed)
│   └── login_api.py
│
├── requirements.txt            # Python dependencies
├── pytest.ini                 # Pytest configuration
├── .flake8                     # Code linting configuration
├── pyproject.toml              # Black & isort configuration
├── .pre-commit-config.yaml     # Pre-commit hooks
├── .env.example                # Environment variables template
└── README.md                   # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Chrome browser (for WebDriver)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd greencity_selenium
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env file with your actual test credentials
   ```

5. **Install pre-commit hooks (optional but recommended):**
   ```bash
   pre-commit install
   ```

### Environment Configuration

Create a `.env` file based on `.env.example` and configure:

```env
# User credentials for testing
USER_EMAIL=your_test_email@example.com
USER_PASSWORD=your_test_password
EXPECTED_USERNAME=your_expected_display_name

# LocalStorage tokens for authenticated sessions
LOCALSTORAGE_accessToken=your_access_token
LOCALSTORAGE_refreshToken=your_refresh_token
LOCALSTORAGE_language=en
LOCALSTORAGE_name=your_username
LOCALSTORAGE_userId=your_user_id
```

## 🧪 Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_login.py

# Run tests with specific marker
pytest -m login

# Run tests with verbose output
pytest -v

# Run tests with Allure reporting
pytest --alluredir=allure-results
```

### Test Markers

The project uses pytest markers for test categorization:

- `@pytest.mark.login` - Login functionality tests
- `@pytest.mark.smoke` - Smoke tests
- `@pytest.mark.regression` - Regression tests
- `@pytest.mark.create_news` - News creation tests

### Generating Allure Reports

```bash
# Generate and open Allure report
allure serve allure-results
```

## 📝 Code Quality

### Linting and Formatting

```bash
# Check code style with flake8
flake8 .

# Format code with black
black .

# Sort imports with isort
isort .

# Run all pre-commit hooks
pre-commit run --all-files
```

### Code Standards

- **Line length**: 120 characters
- **Code style**: Black formatter
- **Import sorting**: isort with black profile
- **Linting**: flake8 with custom configuration
- **Type hints**: Encouraged for better code documentation

## 🏗️ Architecture

### Page Object Model (POM)

The framework follows the Page Object Model pattern:

- **Base Classes**: `Base`, `BasePage`, `BaseComponent`
- **Page Classes**: Represent individual pages (e.g., `EcoNewsListPage`)
- **Component Classes**: Represent reusable UI components (e.g., `Header`)

### Key Design Principles

1. **Separation of Concerns**: Tests, page objects, and configuration are separated
2. **Reusability**: Common functionality in base classes
3. **Maintainability**: Consistent locator strategies and naming conventions
4. **Reliability**: Explicit waits instead of hardcoded sleeps

### Locator Strategy

All locators use consistent tuple format:
```python
ELEMENT_NAME = (By.STRATEGY, "locator_string")
```

## 🔧 Best Practices

### Writing Tests

1. **Use descriptive test names** that explain what is being tested
2. **Add docstrings** to test functions explaining their purpose
3. **Use appropriate pytest markers** for test categorization
4. **Implement proper assertions** with meaningful error messages

### Page Objects

1. **Use explicit waits** instead of `time.sleep()`
2. **Implement type hints** for better code documentation
3. **Add Allure steps** for better reporting
4. **Group related locators** and use consistent naming

### Fixtures

1. **Keep fixtures focused** on specific setup/teardown tasks
2. **Use appropriate fixture scopes** (function, class, module, session)
3. **Clean up resources** in fixture teardown

## 🛠️ Troubleshooting

### Common Issues

1. **Chrome driver issues**: Ensure Chrome browser is updated
2. **Element not found**: Check if locators need updating due to UI changes
3. **Timeout errors**: Increase wait times for slow-loading elements
4. **Authentication issues**: Verify credentials in `.env` file

### Debug Mode

Run tests with debug flags:
```bash
# Run with detailed output
pytest -v -s

# Stop on first failure
pytest -x

# Run specific test with debugging
pytest tests/test_login.py::test_positive_login -v -s
```

## 🤝 Contributing

1. **Follow the code style** guidelines (black, flake8, isort)
2. **Write tests** for new functionality
3. **Update documentation** when making changes
4. **Use pre-commit hooks** to ensure code quality
5. **Create meaningful commit messages**

### Pull Request Process

1. Create a feature branch from `main`
2. Make your changes following the style guidelines
3. Add/update tests as needed
4. Run the full test suite
5. Create a pull request with a clear description

## 📚 Additional Resources

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Framework](https://docs.qameta.io/allure/)
- [Page Object Model Pattern](https://selenium-python.readthedocs.io/page-objects.html)

## 📋 Test Coverage

Current test coverage includes:
- User authentication and login
- News creation and editing
- Search functionality
- Bookmark features
- Tag filtering
- Event management

For detailed test reports, generate Allure reports after test execution.

  Purpose: Contains configuration files, such as settings.ini or config.json. This is used to store parameters that may change between environments (e.g., website URL, login credentials, browser settings).

* `requirements.txt` 📦

  Purpose: A list of all project dependencies (e.g., pytest, selenium). It's used to install all necessary libraries with a single command: pip install -r requirements.txt.

