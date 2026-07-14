from locust import HttpUser, task

from tools.fakers import fake


class OpenDebitCardAccountScenarioUser(HttpUser):
    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number(),
        }
        response = self.client.post("/api/v1/users", json=request)

        # Сохраняем полученные данные, включая ID пользователя
        self.user_data = response.json()

    @task
    def open_debit_card_account(self):
        self.client.post(
            "/api/v1/accounts/open-debit-card-account",
            json={"userId": self.user_data["user"]["id"]},
        )
