import pytest
from appium import webdriver

from config.settings import APPIUM_SERVER_URL, APP_PATH, build_options


@pytest.fixture
def driver():
    if not APP_PATH.exists():
        pytest.fail(
            f"APK not found at {APP_PATH}. Place General-Store.apk next to the "
            "project folder or set APPIUM_APP_PATH."
        )

    session = webdriver.Remote(
        command_executor=APPIUM_SERVER_URL,
        options=build_options(),
    )

    yield session

    session.quit()
