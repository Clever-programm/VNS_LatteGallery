from annotated_types import Le
from pydantic import BaseModel, NonNegativeInt, PositiveInt, StringConstraints
from typing import Annotated, Generic, Literal, TypeVar
from enum import  StrEnum


LoginStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
NameStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
PasswordStr = Annotated[str, StringConstraints(min_length=8, pattern=r"^[a-zA-Z0-9_-]+$")]

PageNumber = NonNegativeInt
PageSize = Annotated[PositiveInt, Le(100)]
ItemT = TypeVar("ItemT")


class Page(Generic[ItemT], BaseModel):
    count: int
    items: list[ItemT]


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
    login: LoginStr
    password: PasswordStr
    name: NameStr


class MyAccountUpdateSchema(BaseModel):
    login: LoginStr
    name: NameStr


class AccountUpdateSchema(BaseModel):
    login: LoginStr
    name: NameStr
    role: AccountRole


class AccountPasswordUpdateSchema(BaseModel):
    password: PasswordStr


class AccountCreateSchema(BaseModel):
    login: LoginStr
    password: PasswordStr
    name: NameStr
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

