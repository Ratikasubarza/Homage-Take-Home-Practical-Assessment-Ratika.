from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class HomePage(BasePage):
    NAME_FIELD = (AppiumBy.ID, "com.androidsample.generalstore:id/nameField")
    COUNTRY_SPINNER = (AppiumBy.ID, "com.androidsample.generalstore:id/spinnerCountry")
    FEMALE_RADIO = (AppiumBy.ID, "com.androidsample.generalstore:id/radioFemale")
    MALE_RADIO = (AppiumBy.ID, "com.androidsample.generalstore:id/radioMale")
    LETS_SHOP_BUTTON = (AppiumBy.ID, "com.androidsample.generalstore:id/btnLetsShop")
    NAME_REQUIRED_TOAST = (AppiumBy.XPATH, '//android.widget.Toast[@text="Please enter your name"]')

    def select_country(self, country: str):
        self.click(self.COUNTRY_SPINNER)
        country_locator = (
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{country}"))',
        )
        self.click(country_locator)

    def enter_name(self, name: str):
        self.type_text(self.NAME_FIELD, name)

    def select_gender(self, gender: str):
        normalized = gender.strip().lower()
        if normalized == "female":
            self.click(self.FEMALE_RADIO)
        elif normalized == "male":
            self.click(self.MALE_RADIO)
        else:
            raise ValueError("gender must be 'Female' or 'Male'")

    def tap_lets_shop(self):
        self.click(self.LETS_SHOP_BUTTON)

    def read_toast(self) -> str:
        toast = WebDriverWait(
            self.driver,
            5,
            poll_frequency=0.1,
        ).until(
            EC.presence_of_element_located(self.NAME_REQUIRED_TOAST)
        )

        return toast.get_attribute("text")

    def complete_form(
        self,
        name: str = "Ratika QA",
        country: str = "Argentina",
        gender: str = "Female",
    ):
        self.select_country(country)
        self.enter_name(name)
        self.select_gender(gender)

    def enter_store(
        self,
        name: str = "Ratika QA",
        country: str = "Argentina",
        gender: str = "Female",
    ):
        self.complete_form(name=name, country=country, gender=gender)
        self.tap_lets_shop()
