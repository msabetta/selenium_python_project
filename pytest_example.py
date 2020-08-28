from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("driver_init")
class BaseTest:
    pass

@pytest.mark.incremental
class TestBooking(BaseTest):

    @pytest.mark.parametrize("url",["http://blazedemo.com/"])
    def test_search_flight(self,url):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get(url)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[value='Find Flights']"))).click()
        assert 0

    def test_choose_any_flight(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Choose This Flight']"))).click()
        text = self.driver.find_element_by_tag_name("h2").text
        #assert text == "Your flight from Paris to Buenos Aires has been reserved."
        assert text