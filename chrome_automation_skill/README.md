# Chrome Automation Skill

## Installation

To install the Chrome Automation Skill, follow these steps:

1. Ensure you have Python 3.x installed on your machine.
2. Install the necessary dependencies:
   ```bash
   pip install selenium
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/ysaisme/ysa-skills.git
   ```
4. Navigate to the `chrome_automation_skill` directory:
   ```bash
   cd ysa-skills/chrome_automation_skill
   ```

## Usage Examples

Here are some basic usage examples for the Chrome Automation Skill:

### Example 1: Open a Website

```python
from chrome_automation_skill import ChromeAutomation

automation = ChromeAutomation()
automation.open_website('https://www.example.com')
```

### Example 2: Fill a Form

```python
automation.fill_form({
    'username': 'test_user',
    'password': 'secure_password'
})
```

## Method Descriptions

### `open_website(url)`

Opens the specified URL in Chrome.

- **Parameters**:
  - `url` (str): The URL of the website to open.

### `fill_form(data)`

Fills out a form with the provided data.

- **Parameters**:
  - `data` (dict): A dictionary containing as key-value pairs where keys are the form field names.

## Best Practices

- Always ensure the Chrome driver is up to date with your version of Chrome.
- Use explicit waits to handle loading times instead of implicit waits for more controlled automation flow.
- Utilize a virtual environment for managing dependencies related to this project.

## Troubleshooting Guide

- **Issue**: Chrome driver not found
  - **Solution**: Ensure that the Chrome driver is installed and its path is set correctly in the system environment variables.

- **Issue**: Automation fails due to element not found
  - **Solution**: Use explicit waits or check the visibility of elements before interacting with them.

For more specific issues, please refer to the official Selenium documentation or contact support.