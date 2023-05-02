from databases import Database
from app.utils.constants import DB_URL, TESTING, TEST_DB_URL

if TESTING:
    db = Database(TEST_DB_URL)
else:
    db = Database(DB_URL)
