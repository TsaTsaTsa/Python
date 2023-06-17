from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from music.models import song, playlist
from music.schemas import Song

router = APIRouter(
    prefix="/song",
    tags=["song"]
)


@router.get("/songs", response_model=List[Song])
async def get_songs(session: AsyncSession = Depends(get_async_session)):
    query = select(song)
    result = await session.execute(query)
    return result.all()


@router.get("/songs/by_id", response_model=List[Song])
async def get_song_by_id(song_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(song).where(song.c.id == song_id)
    result = await session.execute(query)
    return result.all()


@router.post("/playlists")
async def create_playlist(playlist_name: str, session: AsyncSession = Depends(get_async_session)):
    new_playlist = {'name': playlist_name}
    stmt = insert(playlist).values(new_playlist)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/playlists/by_id")
async def add_song_to_playlist(song_id: int, pl_id: int, session: AsyncSession = Depends(get_async_session)):
    pl = select(playlist).where(playlist.c.id == pl_id)
    pl_song = {'id': pl_id, 'name': pl[0].name, 'songs': song_id}
    stmt = insert(playlist).values(pl_song)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/songs/add")
async def add_song(new_song: Song, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(song).values(**new_song.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/songs/ratings")
async def rate_song(song_id: int, rating: int, session: AsyncSession = Depends(get_async_session)):
    stmt = update(song).where(song.c.id == song_id).values(ratings=rating)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
