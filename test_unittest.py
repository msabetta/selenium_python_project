# file test_unittest.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(filename="log.txt", level=logging.INFO)
#https://www.gridlastic.com/grid-configuration.php (for info)

class TestExamples(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="https://4zHLKZSwEHRjpK3cPoT2Ggf24qxdwzAr:Z82AXLWsiDBxeuAUJkNgqS8l9wpvVQNL@l85vex9o-hub.gridlastic.com/wd/hub", #API endpoint Selenium Grid Hub
            desired_capabilities={
                "browserName": "chrome",
                "browserVersion": "latest",
                "video": "True",
                "platform": "WIN10",
                "platformName": "windows",
            })
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Note: driver.maximize_window does not work on Linux, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)

    def test_one(self):
        try:
            driver = self.driver
            driver.get("http://www.python.org")
            self.assertIn("Python", driver.title)
            elem = driver.find_element_by_name("q")
            elem.send_keys("documentation")
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source
        finally:
            VIDEO_URL = "https://s3-eu-central-1.amazonaws.com/kc30ea1a-6y9b-a38c-1e64-t2u8d227g8a9/dda5520c-8083-2bae-08f7-1fb5f9c5280e/play.html?"
            logging.info("Test One Video: " + VIDEO_URL + driver.session_id)

    def test_two(self):
        try:
            driver = self.driver
            driver.get("http://www.google.com")
            elem = driver.find_element_by_name("q")
            elem.send_keys("webdriver")
            elem.send_keys(Keys.RETURN)
        finally:
            VIDEO_URL = "https://s3-eu-central-1.amazonaws.com/kc30ea1a-6y9b-a38c-1e64-t2u8d227g8a9/dda5520c-8083-2bae-08f7-1fb5f9c5280e/play.html?"
            logging.info("Test Two Video: " + VIDEO_URL + driver.session_id)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()