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
