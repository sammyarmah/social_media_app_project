from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

DATABESE_URL = settings.DATABASE_URL_ASYNC

engine = create_async_engine(DATABESE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, exprire_on_commit = True
)

class Base(DeclarativeBase):
    pass