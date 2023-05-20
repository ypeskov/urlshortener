
from typing import Annotated

import uvicorn
from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.routers import url_crud
from app.database import get_db

from app.routers import url_router

app = FastAPI()

app.include_router(url_router.router)


@app.get('/{short_url}', response_class=RedirectResponse, status_code=status.HTTP_301_MOVED_PERMANENTLY)
def redirect_to_full_url(short_url: str, db: Annotated[Session, Depends(get_db)]) -> RedirectResponse:
    db_url = url_crud.get_url_by_short(db, short_url=short_url)
    if db_url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No URL found")
    return RedirectResponse(url=db_url.full_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
