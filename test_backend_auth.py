import pytest
import allure
from Api_Client import ApiClient
from constance import LOGIN, PASSWORD, INVALID_LOGIN, INVALID_PASSWORD

client = ApiClient()

@allure.feature("Авторизация")
class TestAuth:


    @allure.story("Позитивные сценарии авторизации")
    @allure.title("Успешный вход с валидными логином и паролем")
    def test_login_success(self):
        response = client.login(LOGIN, PASSWORD)
        with allure.step(f"POST /login с email={LOGIN} и валидным паролем"):
            assert response.status_code == 200
            data = response.json()
            assert "token" in data and isinstance(data["token"], str)


    @allure.story("Негативные сценарии авторизации")
    @pytest.mark.parametrize("email,password", [
        (INVALID_LOGIN, PASSWORD),
        (LOGIN, INVALID_PASSWORD),
        ("", PASSWORD),
        (LOGIN, ""),
        ("", ""),
        (None, None)
    ])
    @allure.title("Ошибка при невалидных данных входа: email={0}, password={1}")
    def test_login_failures(self, email, password):
        response = client.login(email, password)
        with allure.step(f"POST /login с email={email} и паролем={password}"):
            assert response.status_code != 200
