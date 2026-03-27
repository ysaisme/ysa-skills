# Chrome Automation Skill

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from chrome_skill import ChromeSkill

# Create instance
skill = ChromeSkill(headless=False)

# Open a webpage
skill.open_page("https://www.example.com")

# Fill a form
skill.fill_form({
    'username': 'test_user',
    'password': 'secure_password'
})

# Close browser
skill.close()
```

## Core Methods

### Navigation
- `open_page(url)` - Open a webpage
- `get_page_title()` - Get current page title
- `get_page_url()` - Get current URL
- `get_page_source()` - Get HTML source

### Interaction
- `click_element(selector)` - Click an element
- `input_text(selector, text)` - Type text in a field
- `fill_form(fields)` - Fill multiple form fields
- `submit_form(selector)` - Submit a form
- `scroll(direction, amount)` - Scroll page
- `scroll_to_element(selector)` - Scroll to element

### Data & Content
- `take_screenshot(filename)` - Capture page screenshot
- `extract_data(selectors)` - Extract data using CSS selectors
- `execute_javascript(script)` - Run JavaScript code
- `wait_for_element(selector, timeout)` - Wait for element presence

### Window/Frame Management
- `switch_to_frame(selector)` - Switch to iframe
- `switch_to_default_content()` - Return to main page
- `close()` - Close browser and cleanup

## Usage Examples

### Example 1: Web Search

```python
from chrome_skill import ChromeSkill

skill = ChromeSkill(headless=False)
skill.open_page("https://www.google.com")
skill.input_text('input[name="q"]', "Python Selenium")
skill.submit_form()
skill.wait_for_element('h3', timeout=10)
results = skill.extract_data({'titles': 'h3'})
print(results)
skill.close()
```

### Example 2: Take Screenshot

```python
skill = ChromeSkill(headless=True)
skill.open_page("https://www.example.com")
skill.take_screenshot("example.png")
skill.close()
```

### Example 3: Extract Data

```python
skill = ChromeSkill(headless=True)
skill.open_page("https://news.ycombinator.com")
data = skill.extract_data({
    'titles': '.title a',
    'scores': '.score'
})
print(f"Found {len(data['titles'])} articles")
skill.close()
```

## Selectors

The skill supports all CSS selectors:
- **ID**: `#my-id`
- **Class**: `.my-class`
- **Tag**: `div`, `a`, `input`
- **Attribute**: `input[name="email"]`
- **Descendant**: `div.container`
- **Child**: `ul > li`

## Best Practices

1. **Use explicit waits**: Always wait for elements before interacting
2. **Headless mode**: Use `headless=True` for production (50-70% faster)
3. **Close browser**: Always call `close()` to cleanup resources
4. **Use context managers**: Consider wrapping in try/finally

```python
skill = ChromeSkill()
try:
    skill.open_page("https://example.com")
    # ... your automation code
finally:
    skill.close()
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| ChromeDriver not found | `webdriver-manager` handles this automatically |
| Element not found | Use `wait_for_element()` before interacting |
| Page not loading | Increase wait timeout or check network |
| Headless mode issues | Try `headless=False` for debugging |

## License

MIT
