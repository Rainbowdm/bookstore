from sqlalchemy import (MetaData, create_engine, Table, Column, Integer, Text, ARRAY)
from app.utils.constants import DB_URL

metadata = MetaData()
engine = create_engine(DB_URL)
metadata.create_all(engine)

authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text),
    Column("books", ARRAY(Text))
)
