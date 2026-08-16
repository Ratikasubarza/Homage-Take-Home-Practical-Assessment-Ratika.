from typing import Tuple

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator: Locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator: Locator):
        self.wait.until(lambda driver: len(driver.find_elements(*locator)) > 0)
        return self.driver.find_elements(*locator)

    def click(self, locator: Locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: Locator, value: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def text(self, locator: Locator) -> str:
        return self.find(locator).text

    def is_visible(self, locator: Locator) -> bool:
        try:
            self.find(locator)
            return True
        except Exception:
            return False
