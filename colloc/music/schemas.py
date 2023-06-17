from pydantic import BaseModel


class Song(BaseModel):
    id: int
    name: str
    author: str
    genre: str
    time: str
    album: str
    ratings: int


class Playlist(BaseModel):
    id: int
    name: str
    songs: int
