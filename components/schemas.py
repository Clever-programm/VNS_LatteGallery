from pydantic import BaseModel, StringConstraints

from typing import Annotated
from typing import Literal
from enum import  StrEnum


class StatusResponse(BaseModel):
    status: Literal["ok"]


class AccountRole(StrEnum):
    USER = "USER"
    ADMIN = "ADMIN"
    MAIN_ADMIN = "MAIN_ADMIN"


class UUID(StrEnum):
    UUID = "None"


class AccountSchema(BaseModel):
    id: int
    login: str
    name: str
    role: AccountRole


class AccountRegisterSchema(BaseModel):
    login: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    password: Annotated[str, StringConstraints(min_length=8, pattern=r"^[a-zA-Z0-9 -] +$")]
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class MyAccountUpdateSchema(BaseModel):
    login: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class AccountUpdateSchema(BaseModel):
    login: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    role: AccountRole


class AccountPasswordUpdateSchema(BaseModel):
    password: Annotated[str, StringConstraints(min_length=8, pattern=r"^[a-zA-Z0-9 -] +$")]


class AccountCreateSchema(BaseModel):
    login: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    password: Annotated[str, StringConstraints(min_length=8, pattern=r"^[a-zA-Z0-9 -] +$")]
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    role: AccountRole


class PictureSchema(BaseModel):
    id: int
    title: str
    creation_date_time: str
    tags: list[str]
    is_private: bool
    owner_id: int
    file_uuid: UUID


class PictureCreateSchema(BaseModel):
    title: str
    tags: list[str]
    is_private: bool
    file_uuid: UUID


class PictureUpdateSchema(BaseModel):
    title: str
    tags: list[str]
    is_private: bool


class FileSchema(BaseModel):
    uuid: UUID

