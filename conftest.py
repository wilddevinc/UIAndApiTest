import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from browser_option import generate_chrome_options_remote, generate_chrome_options_local
from config import REMOTE_GRID, URL_PLATFORM, CHROMEDRIVER_PATH, BROWSER_TYPE, BROWSER_VERSION
from application import Application
from constance import DOWNLOAD_DIR
from Api_Client import ApiClient
from constance import LOGIN, PASSWORD


@pytest.fixture(scope="function", autouse=True)
def app():
    if BROWSER_TYPE == 'local':
        options = generate_chrome_options_local(headless=False)  # headless=True или False — по желанию
        service = Service(executable_path=CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=options)

    else:  # remote запуск (например, через selenoid)
        capabilities = {
            "browserName": "chrome",
            "browserVersion": BROWSER_VERSION,
            "selenoid:options": {
                "enableVideo": False,
                "enableVNC": True,
            },
            "pageLoadStrategy": "normal",
        }

        options = generate_chrome_options_remote()
        options.set_capability("browserVersion", capabilities["browserVersion"])
        options.set_capability("pageLoadStrategy", capabilities["pageLoadStrategy"])
        for key, value in capabilities.get("selenoid:options", {}).items():
            options.set_capability(f"selenoid:{key}", value)

        driver = webdriver.Remote(command_executor=REMOTE_GRID, options=options)

    return Application(driver=driver, base_url=URL_PLATFORM)

@pytest.fixture
def wait_for_download():
    """
    Фикстура, которая возвращает функцию ожидания скачивания файла.
    Функция ожидает появления в папке DOWNLOAD_DIR файла,
    имя которого начинается с переданного префикса.

    Использование:
        wait_for_download(prefix, timeout=30)
    """
    def _wait_for_file(prefix, timeout=30):
        end_time = time.time() + timeout
        while time.time() < end_time:
            for fname in os.listdir(DOWNLOAD_DIR):
                if fname.startswith(prefix) and not fname.endswith(".crdownload"):
                    file_path = os.path.join(DOWNLOAD_DIR, fname)
                    if os.path.getsize(file_path) > 0:
                        return True
            time.sleep(1)
        raise TimeoutError(f"Файл с префиксом '{prefix}' не появился в папке {DOWNLOAD_DIR} за {timeout} секунд")

    return _wait_for_file

@pytest.fixture(scope="session")
def token():
    client = ApiClient()
    response = client.login(LOGIN, PASSWORD)
    assert response.status_code == 200
    return response.json()["token"]