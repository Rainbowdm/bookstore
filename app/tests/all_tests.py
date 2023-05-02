import unittest
from starlette.testclient import TestClient
from app.main import app
from app.utils.pure_db import fetch, execute
import asyncio
from app.utils.security import get_hashed_password

client = TestClient(app)
loop = asyncio.get_event_loop()


def insert_user(username, password):
    query = """insert into users(username,password) values(:username,:password)"""
    hashed_password = get_hashed_password(password)
    values = {"username": username, "password": hashed_password}
    loop.run_until_complete(execute(query, False, values))


def check_personal_user(name, mail):
    query = """select * from test.public.personal where name=:name and mail=:mail"""
    values = {"name": name, "mail": mail}
    result = loop.run_until_complete(fetch(query, True, values))
    print(result)
    if result is None:
        return False
    return True


def get_auth_header():
    insert_user("test", "test")
    response = client.post("/token", data=dict(username="test", password="test"))
    jwt_token = response.json()["access_token"]
    auth_header = {"Authorization": f"Bearer {jwt_token}"}
    return auth_header


def clear_db():
    query1 = """delete from test.public.users;"""
    query2 = """delete from test.public.authors;"""
    query3 = """delete from test.public.books;"""
    query4 = """delete from test.public.personal;"""

    loop.run_until_complete(execute(query1, False))
    loop.run_until_complete(execute(query2, False))
    loop.run_until_complete(execute(query3, False))
    loop.run_until_complete(execute(query4, False))


class TestDB(unittest.TestCase):

    def test_token_successful(self):
        insert_user("user1", "pass1")
        response = client.post("/token", data=dict(username="user1", password="pass1"))
        assert response.status_code == 200
        print(response.json())
        assert "access_token" in response.json()
        clear_db()

    def test_token_unauthorized(self):
        insert_user("user1", "pass1")
        response = client.post("/token", data=dict(username="user1", password="pass"))
        assert response.status_code == 401
        clear_db()

    def test_post_user(self):
        auth_header = get_auth_header()
        user_dict = {"name": "user1", "password": "secret", "mail": "a@b.com", "role": "admin"}
        response = client.post("/v1/user", json=user_dict, headers=auth_header)
        print(response.json())
        assert response.status_code == 201
        assert check_personal_user("user1", "a@b.com") == True
        clear_db()

    def test_post_user_wrong_email(self):
        auth_header = get_auth_header()
        user_dict = {"name": "user1", "password": "secret", "mail": "invalid", "role": "admin"}
        response = client.post("/v1/user", json=user_dict, headers=auth_header)
        assert response.status_code == 422
        clear_db()


if __name__ == '__main__':
    unittest.main()
