import aioredis
from app.utils.constants import TESTING, TEST_REDIS_URL

# https://linuxhint.com/query-redis-python/
# redis = None
redis = aioredis.Redis()


async def check_test_redis():
    global redis
    if TESTING:
        redis = await aioredis.from_url(TEST_REDIS_URL)
