# General Store Mobile Automation

Appium test suite for the General Store Android application.

## Test Coverage

- Shows validation when the name is empty.
- Opens the product catalogue after completing the form.
- Adds a product and verifies it appears in the cart.

## Tech Stack

- Python 3.11
- Appium 3 with UiAutomator2
- pytest
- Page Object Model

## Project Structure

```text
general-store-appium/
├── config/
│   └── settings.py
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── home_page.py
│   └── products_page.py
├── tests/
│   ├── conftest.py
│   └── test_general_store.py
├── pytest.ini
└── requirements.txt
```

## Setup

Install Appium and the Android driver:

```bash
npm install -g appium
appium driver install uiautomator2
appium driver doctor uiautomator2
```

Create the Python environment:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The default APK location is one level above the project folder:

```text
QA Tech test/
├── General-Store.apk
└── general-store-appium/
```

Use `APPIUM_APP_PATH` when the APK is stored elsewhere:

```bash
export APPIUM_APP_PATH="/absolute/path/to/General-Store.apk"
```

The default device is `emulator-5554`. Override it when needed:

```bash
export ANDROID_DEVICE_NAME="Pixel_API_35"
export ANDROID_UDID="emulator-5554"
export APPIUM_SERVER_URL="http://127.0.0.1:4723"
```

## Run Tests

Start Appium in a separate terminal:

```bash
appium
```

Run the full suite:

```bash
pytest
```

Run one test:

```bash
pytest tests/test_general_store.py::test_added_product_is_displayed_in_cart -v
```
