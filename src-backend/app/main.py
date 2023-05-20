from fastapi import FastAPI

from .routers import url_router


app = FastAPI()

app.include_router(url_router.router)
