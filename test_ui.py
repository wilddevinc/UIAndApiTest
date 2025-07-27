import allure
from constance import LOGIN, PASSWORD


class TestUi:


    @allure.feature("Авторизация и скачивание отчёта")
    @allure.story("Тест входа и скачивание отчёта устройства")
    def test_ui(self, app, wait_for_download):
        expected_prefix = "devices_report"
        with allure.step("Авторизация пользователя"):
            app.MainPage.authorize(LOGIN, PASSWORD)

        with allure.step("Нажатие кнопки Войти"):
            app.MainPage.step_click_button_submit()

        with allure.step("Выполнение основного UI теста"):
            app.MainPage.step_ui_test()

        with allure.step(f"Проверка, что файл с префиксом '{expected_prefix}' скачался"):
            assert wait_for_download(expected_prefix), "Файл не скачался"

