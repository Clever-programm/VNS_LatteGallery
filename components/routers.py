from fastapi import APIRouter, status

from components.schemas import AccountUpdateSchema, AccountPasswordUpdateSchema, AccountCreateSchema
from schemas import StatusResponse, AccountRegisterSchema, AccountSchema, Role

status_router = APIRouter(prefix="/status")
accounts_router = APIRouter(prefix="/accounts", tags=["Аккаунты"])
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
        password=body.password,
        name=body.name,
        role=Role.USER
    )


@accounts_router.get('/my', summary="Получение данных своего аккаунта", tags=["Аккаунты"])
def get_my_account() -> AccountSchema:
    return AccountSchema(
        id=1,
        login="qwerty",
        password="qwerty",
        name="QWERTY",
        role=Role.USER
    )


@accounts_router.put('/my', summary="Обновление данных своего аккаунта", tags=["Аккаунты"])
def update_my_account(body: AccountUpdateSchema) -> AccountSchema:
    return AccountSchema(
        id=1,
        login=body.login,
        password=body.password,
        name=body.name,
        role=Role.USER
    )


@accounts_router.put('/my/password', summary="Обновить пароль своего аккаунта", tags=["Аккаунты"])
def update_my_account_password(body: AccountPasswordUpdateSchema):
    pass


@accounts_router.post('', summary="Создать новый аккаунт", tags=["Аккаунты"])
def register_account(body: AccountCreateSchema) -> AccountSchema:
    return AccountSchema(
        id=body.id,
        login=body.login,
        password=body.password,
        name=body.name,
        role=Role.USER
    )
