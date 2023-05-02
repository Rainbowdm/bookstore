JW_SECRET_KEY = "96173b4221d1bf4f9630cdfec9878d191db89239e9dd228a90959b405b904502"
JWT_ALGORITH = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 60 * 24 * 5

TOKEN_DESCRIPTION = "It checks username and password. If they are true, it returns JWT token."
TOKEN_SUMMARY = "It returns JWT token"

ISBN_DESCRIPTION = "It is unique identifier for books"

DB_HOST = "localhost"
DB_USER = "admin"
DB_PASSWORD = "admin"
DB_NAME = "bookstore"
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

UPLOAD_PHOTO_APIKEY = "064eeac6cd8f0148ed8ebb5622c5e8b9"
UPLOAD_PHOTO_URL = f"https://api.imgbb.com/1/upload?key={UPLOAD_PHOTO_APIKEY}"

REDIS_URL = "redis://localhost"

TESTING = False
IS_LOAD_TEST = True
TEST_DB_HOST = "localhost"
TEST_DB_USER = "test"
TEST_DB_PASSWORD = "test"
TEST_DB_NAME = "test"
TEST_DB_URL = f"postgresql://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}/{TEST_DB_NAME}"
TEST_REDIS_URL = "redis://localhost"

