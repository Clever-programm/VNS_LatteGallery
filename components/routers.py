from fastapi import APIRouter, status
from pydantic import PositiveInt

from components.schemas import (
    StatusResponse,
    AccountRegisterSchema,
    AccountSchema,
    AccountUpdateSchema,
    AccountPasswordUpdateSchema,
    AccountCreateSchema,
    PictureCreateSchema,
    PictureUpdateSchema,
    PictureSchema,
    FileSchema,
    MyAccountUpdateSchema
)
from schemas import AccountRole, Page, PageNumber, PageSize


status_router = APIRouter(prefix="/status", tags=["Статус"])
accounts_router = APIRouter(prefix="/accounts", tags=["Аккаунты"])
pictures_router = APIRouter(prefix="/pictures", tags=["Картинки"])
files_router = APIRouter(prefix="/files", tags=["Файлы"])

USER: AccountSchema

@status_router.get('', summary="Получить статус сервера", tags=["Статус"])
async def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@accounts_router.post('/register', summary="Регистрация нового аккаунта",
                      tags=["Аккаунты"], status_code=status.HTTP_201_CREATED)
async def register_account(body: AccountRegisterSchema) -> AccountSchema:
    return AccountSchema(
        id=1,
        login=body.login,
        name=body.name,
        role=AccountRole.USER
    )


@accounts_router.get('/my', summary="Получение данных своего аккаунта", tags=["Аккаунты"])
async def get_my_account() -> AccountSchema:
    pass


@accounts_router.put('/my', summary="Обновление данных своего аккаунта", tags=["Аккаунты"])
async def update_my_account(body: MyAccountUpdateSchema) -> AccountSchema:
    return AccountSchema(
        id=1,
        login=body.login,
        name=body.name,
        role=AccountRole.USER
    )


@accounts_router.put('/my/password', summary="Обновить пароль своего аккаунта", tags=["Аккаунты"])
async def update_my_account_password(body: AccountPasswordUpdateSchema):
    pass


@accounts_router.post('', summary="Создать новый аккаунт", tags=["Аккаунты"])
async def create_account(body: AccountCreateSchema) -> AccountSchema:
    return AccountSchema(
        id=1,
        login=body.login,
        name=body.name,
        role=body.role
    )


@accounts_router.get("/{id}", summary="Получение аккаунт по идентификатору")
async def get_account_by_id(id: PositiveInt) -> AccountSchema:
    pass


@accounts_router.get('', summary="Получить список всех аккаунтов", tags=["Аккаунты"])
async def get_all_accounts(page: PageNumber = 0, size: PageSize = 10) -> Page[AccountSchema]:
    return Page(
        count=1,
        items=[],
    )


@accounts_router.put("/{id}", summary="Обновить аккаунт по идентификатору")
async def update_account_by_id(id: PositiveInt, body: AccountUpdateSchema) -> AccountSchema:
    pass


@pictures_router.post("", summary="Создать новую картинку", tags=["Картинки"])
async def create_picture(body: PictureCreateSchema):
    pass


@pictures_router.get("", summary="Получить список всех картинок", tags=["Картинки"])
async def get_all_pictures(page: PageNumber = 0, size: PageSize = 10) -> Page[PictureSchema]:
    return Page(
        count=1,
        items=[],
    )


@pictures_router.get("/my", summary="Получить список своих картинок", tags=["Картинки"])
async def get_my_pictures(page: PageNumber = 0, size: PageSize = 10) -> Page[PictureSchema]:
    return Page(
        count=1,
        items=[],
    )


@pictures_router.get("/{id}", summary="Получить картинку по идентификатору", tags=["Картинки"])
async def get_picture_by_id(id: PositiveInt) -> PictureSchema:
    pass


@pictures_router.put("/{id}", summary="Обновить картинку по идентификатору", tags=["Картинки"])
async def update_picture_by_id(id: PositiveInt, body: PictureUpdateSchema) -> PictureSchema:
    pass


@files_router.post('', summary="Загрузить файл на сервер", tags=["Файлы"])
async def files_upload() -> FileSchema:
    pass


@files_router.get('/{uuid}', summary="Скачать содержимое файла", tags=["Файлы"])
async def files_download(uuid: PositiveInt) -> FileSchema:
    pass



