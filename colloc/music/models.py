from typing import List

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, ARRAY

from music.schemas import Song

metadata = MetaData()

song = Table(
    "song",
    metadata,
    Column("id", Integer, primary_key=True, unique=True),
    Column("name", String, nullable=False),
    Column("author", String, nullable=False, unique=True),
    Column("genre", String, nullable=False),
    Column("time", String, nullable=False),
    Column("album", String),
    Column("ratings", Integer),
)


playlist = Table(
    "playlist",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("songs", Integer)
)

