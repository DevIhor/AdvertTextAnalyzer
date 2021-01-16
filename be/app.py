from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from be.core.db import engine, Base
from be.core.routers import users as users_routes

Base.metadata.create_all(bind=engine)
server = FastAPI(
    title="ATAWA (Advert Text Analyzer Web Application)",
    description="This is a simple web application, that allows you to upload advert as text and "
                "make analyze: how it differs from more popular adverts, which words are used "
                "the most, etc. Web app also allows you to make prediction if this advert may be "
                "popular",
    version="0.0.1"
)

server.mount("/static", StaticFiles(directory="static"), name="static")


@server.get("/")
async def read_root():
    return {"Hello": "World"}


server.include_router(users_routes.router)
