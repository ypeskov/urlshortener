from fastapi import FastAPI

from .routers import test_router

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(test_router.router)
