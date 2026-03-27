class ChromeSkill:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        """Open a web page"""
        self.driver.get(url)

    def fill_form(self, element_selector, value):
        """Fill a form field"""
        element = self.driver.find_element_by_css_selector(element_selector)
        element.clear()
        element.send_keys(value)

    def extract_data(self, element_selector):
        """Extract data from a web element"""
        element = self.driver.find_element_by_css_selector(element_selector)
        return element.text

    def take_screenshot(self, file_path):
        """Take a screenshot and save it to a file"""
        self.driver.save_screenshot(file_path)

    def execute_javascript(self, script):
        """Execute a JavaScript script in the context of the page"""
        self.driver.execute_script(script)