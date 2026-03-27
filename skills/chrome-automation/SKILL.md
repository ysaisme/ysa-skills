# Chrome Automation Skill

## Name
Chrome Automation Skill

## Description
The Chrome Automation Skill provides comprehensive browser automation capabilities for Python developers. It enables automated web page navigation, form filling, data extraction, screenshot capture, and complex user interactions. Built on Selenium 4, it simplifies browser automation with an intuitive API.

## Version
1.0.0

## Author
ysaisme

## Language
Python 3.7+

## Features
- **Automated Web Navigation** — Open URLs, navigate between pages, handle redirects
- **Form Automation** — Fill forms, submit data, interact with form elements
- **User Interaction Simulation** — Click buttons, type text, scroll pages, trigger events
- **Page Element Waiting** — Wait for elements to load dynamically, handle AJAX
- **Data Extraction** — Parse HTML, extract structured data using CSS selectors
- **Visual Capture** — Take screenshots of pages at any state
- **JavaScript Execution** — Run custom JavaScript in the browser context
- **Frame & Window Management** — Switch between frames and popup windows
- **Error Handling** — Comprehensive error handling with meaningful feedback
- **Headless Mode** — Run automation without displaying the browser UI

## Technologies Used
- **Selenium 4** — Web browser automation framework
- **BeautifulSoup 4** — HTML/XML parsing and data extraction
- **webdriver-manager** — Automatic ChromeDriver management
- **Pillow** — Image processing for screenshots
- **Python 3.7+** — Core language

## Dependencies
```
selenium==4.15.2
beautifulsoup4==4.12.2
pillow==10.1.0
webdriver-manager==4.0.1
```

## Core Methods

### Navigation
- `open_page(url, wait_time)` — Open a webpage
- `get_page_url()` — Get current page URL
- `get_page_title()` — Get current page title
- `get_page_source()` — Get HTML source

### Interaction
- `click_element(selector)` — Click an element
- `input_text(selector, text)` — Type text in a field
- `fill_form(fields)` — Fill multiple form fields
- `submit_form(selector)` — Submit a form
- `scroll(direction, amount)` — Scroll page
- `scroll_to_element(selector)` — Scroll to element

### Data & Content
- `take_screenshot(filename)` — Capture page screenshot
- `extract_data(selectors)` — Extract data using selectors
- `execute_javascript(script)` — Run JavaScript code
- `wait_for_element(selector, timeout)` — Wait for element presence

### Window/Frame Management
- `switch_to_frame(selector)` — Switch to iframe
- `switch_to_default_content()` — Return to main page
- `close()` — Close browser and cleanup

## Usage Flow

```
1. Initialize ChromeSkill
   ↓
2. Open a webpage (open_page)
   ↓
3. Interact with page (click, input, scroll)
   ↓
4. Extract data (extract_data, take_screenshot)
   ↓
5. Repeat steps 3-4 as needed
   ↓
6. Close browser (close)
```

## Example Usage

```python
from chrome_skill import ChromeSkill

# Create instance
skill = ChromeSkill(headless=False)

# Navigate
skill.open_page("https://www.google.com")

# Search
skill.input_text('input[name="q"]', "Python")
skill.submit_form()

# Wait and extract
skill.wait_for_element('h3', timeout=10)
results = skill.extract_data({'titles': 'h3'})

# Capture
skill.take_screenshot("results.png")

# Cleanup
skill.close()
```

## Output Artifacts

- **Screenshots** — PNG files captured during automation
- **Extracted Data** — Dictionary with lists of extracted text
- **JavaScript Results** — Return values from executed scripts
- **Page Information** — URLs, titles, and metadata

## Supported Selectors

- **CSS Selectors** (default) — `button.submit`, `input[name="email"]`
- **XPath** — `//button[@class="submit"]`
- **ID** — Direct element IDs
- **Class Name** — Element class names
- **Tag Names** — HTML tag names
- **Link Text** — Text of links

## Performance Considerations

- **Headless Mode** — 50-70% faster execution (recommended)
- **Window Size** — Larger windows consume more memory
- **Wait Timeouts** — Balance between reliability and speed
- **Data Extraction** — BeautifulSoup parsing is very fast

## Platform Support

- ✅ Windows 10/11
- ✅ macOS (Intel & Apple Silicon)
- ✅ Linux (Ubuntu, CentOS, etc.)
- ✅ Docker containers

## Common Use Cases

1. **Web Scraping** — Extract data from websites
2. **Automated Testing** — Test web applications
3. **Form Automation** — Fill and submit forms programmatically
4. **Screen Capture** — Document page states
5. **Data Collection** — Gather information from multiple pages
6. **Performance Testing** — Measure page load times
7. **Content Monitoring** — Track website changes

## Limitations

- Requires Chrome browser to be installed
- Cannot interact with Flash content
- Limited by website rate limiting and anti-bot measures
- JavaScript execution limited to browser context only
- CORS restrictions may affect some operations

## Security Considerations

- Avoid storing credentials in code; use environment variables
- Be respectful of website terms of service
- Implement delays between requests
- Use headless mode in production environments
- Clean up sensitive data from screenshots

## Integration Points

- **Works with** — Any Python project, CI/CD pipelines, Docker
- **Data Sources** — Any website with HTML/CSS interface
- **Output** — Screenshots, CSV files, databases, APIs
- **Extensions** — Can be subclassed for custom functionality

## Testing

The skill includes unit tests covering:
- Page navigation
- Element interactions
- Data extraction
- Error handling
- JavaScript execution

Run tests with: `python -m unittest tests.test_chrome_skill -v`

## Maintenance

- **ChromeDriver** — Automatically managed by webdriver-manager
- **Dependencies** — All pinned to tested versions
- **Compatibility** — Tested with Chrome versions 100+

## Future Enhancements

- [ ] Multi-window/tab support
- [ ] Network request interception
- [ ] Cookie management
- [ ] Proxy support
- [ ] Performance metrics
- [ ] Mobile device emulation
- [ ] PDF capture support
- [ ] Video recording capability

---

**Last Updated:** 2026-03-27 07:38:54  
**Status:** Production Ready