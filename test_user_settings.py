import pytest
import allure
from Api_Client import ApiClient
from constance import LOGIN, PASSWORD, VALID_USER_SETTINGS

client = ApiClient()

@allure.feature("Настройки пользователя")
class TestUserSettings:

    @allure.story("Позитивные сценарии изменения настроек")
    @allure.title("Успешное обновление пользовательских настроек")
    def test_update_user_settings_success(self, token):
        response = client.update_user_settings(token, VALID_USER_SETTINGS)
        with allure.step("PUT /user/settings с валидными данными"):
            assert response.status_code == 200


    @allure.story("Негативные сценарии изменения настроек")
    @pytest.mark.parametrize("field,value", [
        ("name", None),
        ("time_zone", "invalid/timezone"),
        ("events_view_type", 5),
        ("locale", "unknown_locale"),
        ("sip_number", ""),
    ])
    @allure.title("Ошибка при неверных данных поля {0}: {1}")
    def test_update_user_settings_invalid(self, token, field, value):
        payload = VALID_USER_SETTINGS.copy()
        payload[field] = value
        response = client.update_user_settings(token, payload)
        with allure.step(f"PUT /user/settings с неверным {field}={value}"):
            assert response.status_code != 200
