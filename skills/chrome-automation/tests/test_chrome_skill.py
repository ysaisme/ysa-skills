import unittest
import os
from chrome_skill import ChromeSkill


class TestChromeSkill(unittest.TestCase):

    def setUp(self):
        self.skill = ChromeSkill(headless=True)

    def tearDown(self):
        self.skill.close()
        if os.path.exists("test_screenshot.png"):
            os.remove("test_screenshot.png")

    def test_open_page_success(self):
        result = self.skill.open_page('https://www.example.com')
        self.assertTrue(result)

    def test_open_page_invalid_url(self):
        result = self.skill.open_page('invalid-url')
        self.assertFalse(result)

    def test_get_page_title(self):
        self.skill.open_page('https://www.example.com')
        title = self.skill.get_page_title()
        self.assertEqual(title, 'Example Domain')

    def test_get_page_url(self):
        self.skill.open_page('https://www.example.com')
        url = self.skill.get_page_url()
        self.assertIsNotNone(url)
        self.assertIn('example.com', url)

    def test_click_element(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.click_element('a')
        self.assertTrue(result)

    def test_input_text(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.input_text('input[type="text"]', 'test input')
        self.assertTrue(result)

    def test_fill_form(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.fill_form({'input[type="text"]': 'test value'})
        self.assertTrue(result)

    def test_scroll_down(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.scroll(direction='down', amount=500)
        self.assertTrue(result)

    def test_scroll_up(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.scroll(direction='up', amount=500)
        self.assertTrue(result)

    def test_scroll_direction_none(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.scroll(direction='down', amount=500)
        self.assertIsNotNone(result)

    def test_take_screenshot(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.take_screenshot('test_screenshot.png')
        self.assertTrue(result)
        self.assertTrue(os.path.exists('test_screenshot.png'))

    def test_extract_data(self):
        self.skill.open_page('https://www.example.com')
        data = self.skill.extract_data({'title': 'h1'})
        self.assertIsInstance(data, dict)
        self.assertIn('title', data)

    def test_wait_for_element(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.wait_for_element('a', timeout=10)
        self.assertTrue(result)

    def test_execute_javascript(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.execute_javascript('return document.title;')
        self.assertEqual(result, 'Example Domain')

    def test_get_page_source(self):
        self.skill.open_page('https://www.example.com')
        source = self.skill.get_page_source()
        self.assertIsInstance(source, str)
        self.assertIn('html', source.lower())

    def test_scroll_to_element(self):
        self.skill.open_page('https://www.example.com')
        result = self.skill.scroll_to_element('a')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
