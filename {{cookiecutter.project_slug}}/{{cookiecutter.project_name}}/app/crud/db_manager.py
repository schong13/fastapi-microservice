from app.schema.users import UserIn, UserOut, UserUpdate
from app.crud.db import database
from app.api.router import users

async def add_user(payload: UserIn):
    query = users.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_user(id):
    query = users.select(users.c.id==id)
    return await database.fetch_one(query=query)
