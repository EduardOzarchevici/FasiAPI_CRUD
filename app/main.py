from fastapi import FastAPI, Depends
from core.database import engine, Base
from routers.user_router import router as user_router
from schemas.user_schemas import UserCreate, UserRead, UserUpdate
from users.fastapi_users import fastapi_users, auth_backend

app = FastAPI()

# Creează tabelele în DB
#Base.metadata.create_all(bind=engine)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)



@app.get("/protected-route")
def protected_route(user=Depends(fastapi_users.current_user(active=True))):
    return {"message": f"Salut, {user.name}! Ești autentificat."}

# Înregistrează routerul
app.include_router(user_router, prefix="/users", tags=["Users"])
