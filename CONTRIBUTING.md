# Contributing to GreenCity Selenium Framework

Thank you for your interest in contributing to the GreenCity Selenium test automation framework! This guide will help you understand how to contribute effectively.

## 🚀 Getting Started

### Development Environment Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/your-username/greencity_selenium.git
   cd greencity_selenium
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install development tools:**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

5. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your test credentials
   ```

## 📋 Code Standards

### Code Style

We enforce consistent code style using automated tools:

- **Black**: Code formatter with 120 character line length
- **isort**: Import statement organizer
- **flake8**: Linting and style checking

### Before Committing

Run these commands to ensure code quality:

```bash
# Format code
black .

# Sort imports
isort .

# Check linting
flake8 .

# Run all pre-commit hooks
pre-commit run --all-files
```

### Code Quality Guidelines

1. **Type Hints**: Add type hints to all function parameters and return values
2. **Docstrings**: Document all classes and public methods
3. **Naming Conventions**: 
   - Classes: `PascalCase`
   - Functions/methods: `snake_case`
   - Constants: `UPPER_SNAKE_CASE`
   - Variables: `snake_case`

4. **Locator Strategy**: Use consistent tuple format:
   ```python
   ELEMENT_NAME = (By.STRATEGY, "locator_string")
   ```

5. **Explicit Waits**: Always use explicit waits instead of `time.sleep()`:
   ```python
   # Good
   element = self.get_wait().until(EC.element_to_be_clickable(locator))
   
   # Bad
   time.sleep(5)
   element = self.driver.find_element(*locator)
   ```

## 🧪 Testing Guidelines

### Writing Tests

1. **Test Organization**: Group related tests in appropriately named test files
2. **Test Names**: Use descriptive names that explain what is being tested
3. **Markers**: Use pytest markers for test categorization:
   ```python
   @pytest.mark.smoke
   @pytest.mark.regression
   @pytest.mark.login
   ```

4. **Test Documentation**: Add docstrings explaining test purpose:
   ```python
   def test_user_can_create_news_article():
       """Test that authenticated user can successfully create a news article.
       
       This test verifies the complete news creation workflow including
       navigation, form filling, and successful publication.
       """
   ```

### Page Objects

1. **Single Responsibility**: Each page object should represent one page or component
2. **Inheritance**: Use base classes (`BasePage`, `BaseComponent`) for common functionality
3. **Method Chaining**: Return page objects to enable fluent interfaces:
   ```python
   def click_submit(self) -> "ResultPage":
       self.submit_button.click()
       return ResultPage(self.driver)
   ```

4. **Error Handling**: Add proper exception handling with meaningful error messages

### Fixtures

1. **Scope Appropriately**: Use the narrowest possible fixture scope
2. **Clean Up**: Ensure fixtures properly clean up resources
3. **Parameterization**: Use parametrized fixtures for test variations

## 🔄 Workflow

### Branch Strategy

1. **Feature Branches**: Create feature branches from `main`
   ```bash
   git checkout -b feature/improve-login-tests
   ```

2. **Bug Fixes**: Create bugfix branches for issues
   ```bash
   git checkout -b bugfix/fix-search-timeout
   ```

### Pull Request Process

1. **Before Creating PR**:
   - Ensure all tests pass
   - Run code quality checks
   - Update documentation if needed
   - Add/update tests for new functionality

2. **PR Description**:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Reference any related issues
   - Include screenshots for UI changes

3. **Review Process**:
   - Address all reviewer feedback
   - Keep commits focused and atomic
   - Squash commits if requested

### Commit Messages

Use clear, descriptive commit messages:

```bash
# Good
git commit -m "Add type hints to EcoNewsListPage methods"
git commit -m "Fix timeout issue in search functionality"
git commit -m "Update README with setup instructions"

# Bad
git commit -m "Fix stuff"
git commit -m "Updates"
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment**: OS, Python version, browser version
2. **Steps to Reproduce**: Clear, numbered steps
3. **Expected vs Actual Behavior**: What should happen vs what happens
4. **Error Messages**: Full error messages and stack traces
5. **Screenshots**: If applicable

## 💡 Feature Requests

For feature requests, please provide:

1. **Use Case**: Why this feature is needed
2. **Detailed Description**: What the feature should do
3. **Acceptance Criteria**: How to know the feature is complete
4. **Alternatives Considered**: Other approaches you've thought about

## 📚 Documentation

### When to Update Documentation

- Adding new page objects or components
- Changing existing APIs or interfaces
- Adding new test markers or categories
- Modifying setup or configuration procedures

### Documentation Standards

- Keep documentation up-to-date with code changes
- Use clear, concise language
- Include code examples where helpful
- Add screenshots for UI-related changes

## 🔍 Code Review Guidelines

### For Reviewers

1. **Focus Areas**:
   - Code correctness and functionality
   - Test coverage and quality
   - Code style and maintainability
   - Documentation completeness

2. **Constructive Feedback**:
   - Suggest improvements, don't just point out problems
   - Explain the reasoning behind suggestions
   - Be respectful and professional

### For Contributors

1. **Responding to Feedback**:
   - Address all comments
   - Ask questions if feedback is unclear
   - Make requested changes or explain why not

2. **Self-Review**:
   - Review your own PR before requesting review
   - Check for common issues (unused imports, debugging code, etc.)

## 🎯 Testing Strategy

### Test Categories

1. **Smoke Tests** (`@pytest.mark.smoke`): Basic functionality checks
2. **Regression Tests** (`@pytest.mark.regression`): Comprehensive test suite
3. **Feature Tests**: Specific feature functionality
4. **Integration Tests**: End-to-end workflows

### Test Data Management

- Use configuration files for test data
- Avoid hardcoded values in tests
- Create reusable test data fixtures
- Keep test data separate from test logic

## 🛠️ Troubleshooting

### Common Issues

1. **Import Errors**: Check PYTHONPATH and virtual environment
2. **WebDriver Issues**: Ensure browser and driver versions match
3. **Timeout Errors**: Increase wait times or improve element selection
4. **Flaky Tests**: Add proper waits and improve element stability

### Getting Help

- Check existing issues and documentation first
- Ask questions in PR discussions
- Create detailed issue reports for bugs
- Reach out to maintainers for guidance

## 📋 Checklist

Before submitting a PR, ensure:

- [ ] Code follows style guidelines (black, flake8, isort)
- [ ] All tests pass locally
- [ ] New functionality includes tests
- [ ] Documentation is updated
- [ ] Pre-commit hooks pass
- [ ] PR description is clear and complete
- [ ] No debugging code or temporary files included

Thank you for contributing to the GreenCity Selenium framework! 🌱