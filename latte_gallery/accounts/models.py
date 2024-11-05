from enum import StrEnum

from latte_gallery.core.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Role(StrEnum):
    USER = "USER"
    ADMIN = "ADMIN"
    MAIN_ADMIN = "MAIN_ADMIN"


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    name: Mapped[str]
    role: Mapped[Role]
