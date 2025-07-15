# from fastapi_users import FastAPIUsers
# from fastapi_users.db import SQLAlchemyUserDatabase
# from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
# from models.user_model import User
# from core.database import get_db  # exemplu, tu adaptează după cum ai definit
# from schemas.user_schemas import UserCreate, UserUpdate, UserDB
#
# SECRET = "SECRET_KEY_MARE_SI_SIGUR"
#
# bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
#
# def get_jwt_strategy() -> JWTStrategy:
#     return JWTStrategy(secret=SECRET, lifetime_seconds=3600)
#
# auth_backend = AuthenticationBackend(
#     name="jwt",
#     transport=bearer_transport,
#     get_strategy=get_jwt_strategy,
# )
#
# async def get_user_db():
#     async with get_db() as session:
#         yield SQLAlchemyUserDatabase(UserDB, session, User)
#
# fastapi_users = FastAPIUsers[UserCreate, UserUpdate, UserDB](
#     get_user_db,
#     [auth_backend],
# )
#
# jwt_authentication = auth_backend
