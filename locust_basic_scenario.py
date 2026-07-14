from locust import HttpUser, between, task


class BasicScenarioUser(HttpUser):
    wait_time = between(5, 10)

    @task(2)
    def get_data(self):
        self.client.get("/get")

    @task(1)
    def post_data(self):
        self.client.get("/post")

    @task(1)
    def delete_data(self):
        self.client.get("/delete")
