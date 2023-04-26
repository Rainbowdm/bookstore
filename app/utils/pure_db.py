import asyncio
from databases import Database
from constants import DB_URL
from orm_db import authors


async def connect_db():
    db = Database(DB_URL)
    await db.connect()
    return db


async def disconnect_db(db):
    await db.disconnect()


query = "insert into books values (:isbn, :name, :author, :year)"
values = [
    {"isbn": "isbn1", "name": "book1", "author": "author1", "year": 2019},
    {"isbn": "isbn2", "name": "book2", "author": "author2", "year": 2020}
]


async def execute(query, is_many, values=None):
    db = await connect_db()
    if is_many:
        await db.execute_many(query=query, values=values)
    else:
        await db.execute(query=query, values=values)
    await disconnect_db(db)


async def fetch(query, is_one, values=None):
    db = await connect_db()
    if is_one:
        result = await db.fetch_one(query=query, values=values)
        out = dict(result)
    else:
        result = await db.fetch_all(query=query, values=values)
        out = []
        for row in result:
            out.append(dict(row))
    await disconnect_db(db)
    print(out)
    return out


# query = "insert into books values (:custom, :name, :author, :year)"
# values = [
#     {"custom": "isbn2", "name": "book2", "author": "author2", "year": 2021},
#     {"custom": "isbn3", "name": "book3", "author": "author3", "year": 2022}
# ]

# query = "select * from books where isbn=:isbn"
# values = {"isbn": "isbn2"}

# query = "select * from books"

# loop = asyncio.get_event_loop()
# loop.run_until_complete(execute(query, True, values))
# loop.run_until_complete(fetch(query, True, values))
# loop.run_until_complete(fetch(query, False))


async def test_orm():
    # query = authors.insert().values(id=1, name="author1", books=["book1", "book2"])
    query = authors.select().where(authors.c.id == 2)
    # await execute(query, False)
    await fetch(query, True)


loop = asyncio.get_event_loop()
loop.run_until_complete(test_orm())
