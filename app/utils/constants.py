import os
from dotenv import load_dotenv

# Create .env file and add parameters
load_dotenv()

JW_SECRET_KEY = os.getenv("JW_SECRET_KEY")
JWT_ALGORITH = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 60 * 24 * 5

TOKEN_DESCRIPTION = (
    "It checks username and password. If they are true, it returns JWT token."
)
TOKEN_SUMMARY = "It returns JWT token"

ISBN_DESCRIPTION = "It is unique identifier for books"

DB_HOST = os.getenv("DB_HOST")
DB_HOST_PRODUCTION = os.getenv("DB_HOST_PRODUCTION")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
DB_URL_PRODUCTION = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST_PRODUCTION}/{DB_NAME}"
)

UPLOAD_PHOTO_APIKEY = os.getenv("UPLOAD_PHOTO_APIKEY")
UPLOAD_PHOTO_URL = f"https://api.imgbb.com/1/upload?key={UPLOAD_PHOTO_APIKEY}"

REDIS_URL = os.getenv("REDIS_URL")
REDIS_URL_PRODUCTION = os.getenv("REDIS_URL_PRODUCTION")

TESTING = True
IS_LOAD_TEST = False
os.environ["PRODUCTION"] = "PRODUCTION"
IS_PRODUCTION = True if os.environ["PRODUCTION"] == "true" else False

TEST_DB_HOST = os.getenv("TEST_DB_HOST")
TEST_DB_USER = os.getenv("TEST_DB_USER")
TEST_DB_PASSWORD = os.getenv("TEST_DB_PASSWORD")
TEST_DB_NAME = os.getenv("TEST_DB_NAME")
TEST_DB_URL = (
    f"postgresql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}/{TEST_DB_NAME}"
)
TEST_REDIS_URL = os.getenv("TEST_REDIS_URL")

JWT_EXPIRED_MSG = "Your JWT token is expired! Renew the JWT token!"
JWT_INVALID_MSG = "Invalid JWT token!"
TOKEN_INVALID_CREDENTIALS_MSG = "Invalid username, password match !"
JWT_WRONG_ROLE = "Unauthorized role!"
