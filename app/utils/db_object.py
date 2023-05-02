from databases import Database
from app.utils.constants import DB_URL, TESTING, TEST_DB_URL, IS_LOAD_TEST

if TESTING or IS_LOAD_TEST:
    db = Database(TEST_DB_URL)
else:
    db = Database(DB_URL)
