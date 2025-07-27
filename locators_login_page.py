from selenium.webdriver.common.by import By


class Login(object):


    LOGIN_INPUT = (By.ID, 'email')
    PASS_INPUT = (By.ID, 'password')
    SUBMIT_BT = (By.XPATH, '/html/body/main/div[2]/div[1]/div/form/div[4]/button')
    DEVICES_ONLINE = (By.XPATH, "//*[contains(text(), 'Устройств сейчас на линии')]")
    CHANGE_COLUMNS = (By.XPATH, '//*[@data-target=".device-table-column-switcher"]')
    DEVICE_MENU_CLOSE = (By.CLASS_NAME,'close')
    DOWNLOAD_REPORT_BUTTON = (By.NAME, "export")
    SUCCESSFULY_DOWNLOAD_POPUP = (By.XPATH, "/html/body/main/div[5]/div/div/div")
    DOWNLOAD_LINK = (By.XPATH, "//*[contains(text(), 'devices_report')]")
