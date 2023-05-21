from pprint import pprint
from typing import Annotated

import uvicorn
from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.routers import url_crud
from app.database import get_db

from app.routers import url_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(url_router.router)


@app.get('/', response_class=RedirectResponse, status_code=status.HTTP_301_MOVED_PERMANENTLY)
async def go_to_add_url():
    return RedirectResponse(app.url_path_for('add_url'),
                            status_code=status.HTTP_301_MOVED_PERMANENTLY)

@app.get('/{short_url}', response_class=RedirectResponse, status_code=status.HTTP_301_MOVED_PERMANENTLY)
def redirect_to_full_url(db: Annotated[Session, Depends(get_db)],
                         short_url: str = None) -> RedirectResponse:
    db_url = url_crud.get_url_by_short(db, short_url=short_url)
    if db_url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No URL found**")
    return RedirectResponse(url=db_url.full_url, status_code=status.HTTP_301_MOVED_PERMANENTLY)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
