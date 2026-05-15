from datetime import datetime
from typing import TYPE_CHECKING
from app.core.db_async import Base
from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

if TYPE_CHECKING:
    from app.models.posts import Post


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(20), default="user")
    bio: Mapped[str] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(server_default=func.now(), onupdate=func.now())


    # Relationships
    # posts: Mapped[list["Post"]] = relationship("Post", back_populates="owner")


