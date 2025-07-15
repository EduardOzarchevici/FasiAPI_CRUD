from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_async_session
from controllers.user_controller import *
from schemas.user_schemas import UserOut, UserBase, UserUpdate, UserPatch
from uuid import UUID


router = APIRouter()

@router.get('/', response_model=list[UserOut])
async def get_users(db: AsyncSession = Depends(get_async_session )):
    return await get_all_users(db)

@router.get('/{user_id}', response_model=UserOut)
async def get_user(user_id: UUID, db: AsyncSession = Depends(get_async_session )):
    return await get_user_by_id(db, user_id)

@router.post('/', response_model=UserOut)
async def create_new_user(user: UserBase, db: AsyncSession = Depends(get_async_session )):
    return await create_user(db, user)

@router.delete('/{user_id}')
async def delete_user(user_id: UUID, db: AsyncSession = Depends(get_async_session )):
    return await delete_by_id(db, user_id)

@router.put('/{user_id}', response_model=UserOut)
async def update_user(user: UserUpdate, user_id: UUID, db: AsyncSession = Depends(get_async_session )):
    return await update_by_id(db, user_id, user)

@router.patch('/{user_id}', response_model=UserOut)
async def patch_user(user_id: UUID, user_data: UserPatch, db: AsyncSession = Depends(get_async_session )):
    return await patch_user_by_id(db, user_id, user_data)
