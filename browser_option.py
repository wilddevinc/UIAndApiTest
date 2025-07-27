from selenium.webdriver.chrome.options import Options
from constance import DOWNLOAD_DIR

def generate_chrome_options_local(headless=False):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")

    prefs = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
    }
    options.add_experimental_option("prefs", prefs)

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    return options

def generate_chrome_options_remote():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless=new')
    return options