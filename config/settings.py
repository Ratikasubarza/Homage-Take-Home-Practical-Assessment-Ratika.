import os
from pathlib import Path

from appium.options.android import UiAutomator2Options


ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_APP_PATH = ROOT_DIR.parent / "General-Store.apk"

APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
APP_PATH = Path(os.getenv("APPIUM_APP_PATH", str(DEFAULT_APP_PATH))).expanduser().resolve()
DEVICE_NAME = os.getenv("ANDROID_DEVICE_NAME", "emulator-5554")
UDID = os.getenv("ANDROID_UDID")


def build_options() -> UiAutomator2Options:
    """Build Appium capabilities for the General Store Android APK."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = DEVICE_NAME
    options.app = str(APP_PATH)
    options.no_reset = False
    options.new_command_timeout = 120
    options.set_capability("appium:autoGrantPermissions", True)

    if UDID:
        options.udid = UDID

    return options
