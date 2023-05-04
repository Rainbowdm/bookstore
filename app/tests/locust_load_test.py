import uvicorn
from locust import HttpUser, TaskSet, task

from app.main import app


class BookstoreLocustTask(TaskSet):

    # @task
    # def token_test(self):
    #     self.client.post("/token", data=dict(username="test", password="test"))

    @task
    def test_post_user(self):
        user_dict = {"name": "personal1", "password": "pass1", "mail": "a@b.com", "role": "admin"}
        auth_header = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0Iiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjgzNDc5NjkxfQ.yPeNVYGPBOTd2VFQbU8ukMInhscdyjRpMsc8tNVDIaA"}
        self.client.post("/v1/user", json=user_dict, headers=auth_header)


class BookstoreLoadTest(HttpUser):
    tasks = [BookstoreLocustTask]
    host = "http://localhost:8000"


# locust -f ./app/tests/locust_load_test.py
if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='127.0.0.1')

# ApacheBench
# ab -n 100 -c 5 -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0Iiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNjgzNDc5NjkxfQ.yPeNVYGPBOTd2VFQbU8ukMInhscdyjRpMsc8tNVDIaA" -p ./app/tests/ab_jsons/post_user.json http://127.0.0.1:8000/v1/user
# Example command
# ab -n 100 -c 10 -H "" -p http://127.0.0.1:8000/v1/user
