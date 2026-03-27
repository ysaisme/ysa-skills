"""
Chrome Automation Skill - Core Module
Author: ysaisme
Version: 1.0.0
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

class ChromeSkill:
    """Browser automation skill using Selenium."""
    
    def __init__(self, headless=True, window_size="1920,1080"):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--window-size={window_size}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        print("✓ Chrome driver initialized")
    
    def open_page(self, url):
        try:
            self.driver.get(url)
            print(f"✓ Opened: {url}")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def click_element(self, selector):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            element.click()
            print(f"✓ Clicked: {selector}")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def input_text(self, selector, text, clear_first=True):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            if clear_first:
                element.clear()
            element.send_keys(text)
            print(f"✓ Typed: {text}")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def fill_form(self, fields):
        try:
            for selector, value in fields.items():
                self.input_text(selector, value)
            print(f"✓ Filled {len(fields)} fields")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def submit_form(self, selector=None):
        try:
            if selector:
                self.click_element(selector)
            else:
                buttons = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="submit"], button[type="submit"]')
                if buttons:
                    buttons[0].click()
            print("✓ Form submitted")
            time.sleep(2)
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def scroll(self, direction="down", amount=500):
        try:
            if direction.lower() == "down":
                self.driver.execute_script(f"window.scrollBy(0, {amount});")
            else:
                self.driver.execute_script(f"window.scrollBy(0, -{amount});")
            print(f"✓ Scrolled {direction}")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def scroll_to_element(self, selector):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, selector)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            print(f"✓ Scrolled to: {selector}")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def take_screenshot(self, filename="screenshot.png"):
        try:
            self.driver.save_screenshot(filename)
            print(f"✓ Screenshot: {filename}")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def extract_data(self, selectors):
        try:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = {}
            for name, selector in selectors.items():
                elements = soup.select(selector)
                results[name] = [elem.get_text(strip=True) for elem in elements]
            print(f"✓ Extracted data")
            return results
        except Exception as e:
            print(f"✗ Error: {e}")
            return {}
    
    def wait_for_element(self, selector, timeout=10):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            print(f"✓ Found: {selector}")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def execute_javascript(self, script):
        try:
            result = self.driver.execute_script(script)
            print("✓ JavaScript executed")
            return result
        except Exception as e:
            print(f"✗ Error: {e}")
            return None
    
    def get_page_title(self):
        return self.driver.title
    
    def get_page_url(self):
        return self.driver.current_url
    
    def get_page_source(self):
        return self.driver.page_source
    
    def switch_to_frame(self, selector):
        try:
            frame = self.driver.find_element(By.CSS_SELECTOR, selector)
            self.driver.switch_to.frame(frame)
            print(f"✓ Switched to frame")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def switch_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
            print("✓ Switched to default")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def close(self):
        try:
            if self.driver:
                self.driver.quit()
                print("✓ Browser closed")
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
