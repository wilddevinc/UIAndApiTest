import requests

class ApiClient:
    BASE_URL = "https://stage-mgt.antisleep.ru/api/v1.00/public"

    def login(self, email, password):
        url = f"{self.BASE_URL}/login"
        payload = {"email": email, "password": password}
        response = requests.post(url, json=payload)
        return response

    def update_user_settings(self, token, data):
        url = f"{self.BASE_URL}/user/settings"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.put(url, json=data, headers=headers)
        return response
