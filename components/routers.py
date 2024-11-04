from fastapi import APIRouter, status

from components.schemas import AccountUpdateSchema, AccountPasswordUpdateSchema, AccountCreateSchema, \
    PictureCreateSchema, PictureSchema, FileSchema, MyAccountUpdateSchema
from schemas import StatusResponse, AccountRegisterSchema, AccountSchema, AccountRole

status_router = APIRouter(prefix="/status", tags=["Статус"])
accounts_router = APIRouter(prefix="/accounts", tags=["Аккаунты"])
pictures_router = APIRouter(prefix="/pictures", tags=["Картинки"])
files_router = APIRouter(prefix="/files", tags=["Файлы"])
USER: AccountSchema

@status_router.get('', summary="Получить статус сервера", tags=["Статус"])
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@accounts_router.post('/register', summary="Регистрация нового аккаунта",
                      tags=["Аккаунты"], status_code=status.HTTP_201_CREATED)
def register_account(body: AccountRegisterSchema) -> AccountSchema:
    return AccountSchema(
        id=1,
        login=body.login,
        name=body.name,
        role=AccountRole.USER
    )


@accounts_router.get('/my', summary="Получение данных своего аккаунта", tags=["Аккаунты"])
def get_my_account() -> AccountSchema:
    return AccountSchema(
        id=1,
        login="qwerty",
        name="QWERTY",
        role=AccountRole.USER
    )


@accounts_router.put('/my', summary="Обновление данных своего аккаунта", tags=["Аккаунты"])
def update_my_account(body: MyAccountUpdateSchema) -> AccountSchema:
    return AccountSchema(
        id=1,
        login=body.login,
        name=body.name,
        role=AccountRole.USER
    )


@accounts_router.put('/my/password', summary="Обновить пароль своего аккаунта", tags=["Аккаунты"])
def update_my_account_password(body: AccountPasswordUpdateSchema):
    pass


@accounts_router.post('', summary="Создать новый аккаунт", tags=["Аккаунты"])
def create_account(body: AccountCreateSchema) -> AccountSchema:
    return AccountSchema(
        id=1,
        login=body.login,
        name=body.name,
        role=body.role
    )


@accounts_router.get('', summary="Получить список всех аккаунтов", tags=["Аккаунты"])
def get_all_accounts() -> list[AccountSchema]:
    pass


@pictures_router.post("", summary="Создать новую картинку", tags=["Картинки"])
def create_picture(body: PictureCreateSchema):
    pass


@pictures_router.get("", summary="Получить список всех картинок", tags=["Картинки"])
def get_all_pictures() -> list[PictureSchema]:
    pass


@pictures_router.get("/my", summary="Получить список своих картинок", tags=["Картинки"])
def get_my_pictures() -> list[PictureSchema]:
    pass


@files_router.post('', summary="Загрузить файл на сервер", tags=["Файлы"])
def files_upload() -> FileSchema:
    pass



