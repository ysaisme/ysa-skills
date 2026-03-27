"""
Chrome Automation Skill - Core Module
Author: ysaisme
Version: 1.0.0
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException,
    StaleElementReferenceException
)
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ChromeSkill:
    """Browser automation skill using Selenium."""

    def __init__(self, headless=True, window_size="1920,1080", wait_timeout=10):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--window-size={window_size}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, wait_timeout)
            logger.info("Chrome driver initialized")
        except WebDriverException as e:
            logger.error(f"Failed to initialize Chrome driver: {e}")
            raise

    def open_page(self, url):
        try:
            self.driver.get(url)
            logger.info(f"Opened: {url}")
            return True
        except WebDriverException as e:
            logger.error(f"Failed to open page: {e}")
            return False

    def click_element(self, selector):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            element.click()
            logger.info(f"Clicked: {selector}")
            return True
        except TimeoutException:
            logger.error(f"Timeout waiting for element to be clickable: {selector}")
            return False
        except StaleElementReferenceException:
            logger.error(f"Element stale: {selector}")
            return False
        except WebDriverException as e:
            logger.error(f"Failed to click element: {e}")
            return False

    def input_text(self, selector, text, clear_first=True):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            if clear_first:
                element.clear()
            element.send_keys(text)
            logger.info(f"Typed: {text}")
            return True
        except TimeoutException:
            logger.error(f"Timeout waiting for element: {selector}")
            return False
        except StaleElementReferenceException:
            logger.error(f"Element stale: {selector}")
            return False
        except WebDriverException as e:
            logger.error(f"Failed to input text: {e}")
            return False

    def fill_form(self, fields):
        try:
            for selector, value in fields.items():
                self.input_text(selector, value)
            logger.info(f"Filled {len(fields)} fields")
            return True
        except Exception as e:
            logger.error(f"Failed to fill form: {e}")
            return False

    def submit_form(self, selector=None):
        try:
            if selector:
                return self.click_element(selector)
            else:
                submit_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="submit"], button[type="submit"]')
                if submit_buttons:
                    submit_buttons[0].click()
                    logger.info("Form submitted")
                    return True
                logger.warning("No submit button found")
                return False
        except WebDriverException as e:
            logger.error(f"Failed to submit form: {e}")
            return False

    def scroll(self, direction="down", amount=500):
        try:
            if direction.lower() == "down":
                self.driver.execute_script(f"window.scrollBy(0, {amount});")
            else:
                self.driver.execute_script(f"window.scrollBy(0, -{amount});")
            logger.info(f"Scrolled {direction}")
            return True
        except WebDriverException as e:
            logger.error(f"Failed to scroll: {e}")
            return False

    def scroll_to_element(self, selector):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, selector)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            logger.info(f"Scrolled to: {selector}")
            return True
        except NoSuchElementException:
            logger.error(f"Element not found: {selector}")
            return False
        except WebDriverException as e:
            logger.error(f"Failed to scroll to element: {e}")
            return False

    def take_screenshot(self, filename="screenshot.png"):
        try:
            self.driver.save_screenshot(filename)
            logger.info(f"Screenshot saved: {filename}")
            return True
        except WebDriverException as e:
            logger.error(f"Failed to take screenshot: {e}")
            return False

    def extract_data(self, selectors):
        try:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = {}
            for name, selector in selectors.items():
                elements = soup.select(selector)
                results[name] = [elem.get_text(strip=True) for elem in elements]
            logger.info(f"Extracted {len(results)} data fields")
            return results
        except Exception as e:
            logger.error(f"Failed to extract data: {e}")
            return {}

    def wait_for_element(self, selector, timeout=10):
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            logger.info(f"Element found: {selector}")
            return True
        except TimeoutException:
            logger.error(f"Timeout waiting for element: {selector}")
            return False
        except WebDriverException as e:
            logger.error(f"Failed to wait for element: {e}")
            return False

    def execute_javascript(self, script):
        try:
            result = self.driver.execute_script(script)
            logger.info("JavaScript executed")
            return result
        except WebDriverException as e:
            logger.error(f"JavaScript execution failed: {e}")
            return None

    def get_page_title(self):
        try:
            return self.driver.title
        except WebDriverException as e:
            logger.error(f"Failed to get page title: {e}")
            return None

    def get_page_url(self):
        try:
            return self.driver.current_url
        except WebDriverException as e:
            logger.error(f"Failed to get page URL: {e}")
            return None

    def get_page_source(self):
        try:
            return self.driver.page_source
        except WebDriverException as e:
            logger.error(f"Failed to get page source: {e}")
            return None

    def switch_to_frame(self, selector):
        try:
            frame = self.driver.find_element(By.CSS_SELECTOR, selector)
            self.driver.switch_to.frame(frame)
            logger.info(f"Switched to frame: {selector}")
            return True
        except NoSuchElementException:
            logger.error(f"Frame not found: {selector}")
            return False
        except WebDriverException as e:
            logger.error(f"Failed to switch to frame: {e}")
            return False

    def switch_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
            logger.info("Switched to default content")
            return True
        except WebDriverException as e:
            logger.error(f"Failed to switch to default content: {e}")
            return False

    def close(self):
        try:
            if self.driver:
                self.driver.quit()
                logger.info("Browser closed")
            return True
        except WebDriverException as e:
            logger.error(f"Failed to close browser: {e}")
            return False
