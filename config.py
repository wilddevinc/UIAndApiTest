import os

CHROMEDRIVER_PATH = "C:\\Test-UI\\chromedriver.exe" # адрес до файла с драйвром, если запускать локально.

BROWSER_NAME = os.environ.get("BROWSER_NAME", "chrome")
BROWSER_VERSION = os.environ.get("BROWSER_VERSION", "138")
BROWSER_TYPE = os.environ.get("BROWSER_TYPE", "local")  # 'local' или 'remote' . локально или selenoid

URL_PLATFORM = os.environ.get("URL_PLATFORM", "https://stage-mgt.antisleep.ru/")
REMOTE_GRID = os.environ.get("REMOTE_GRID", "http://192.168.1.170:4444")