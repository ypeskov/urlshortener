from pprint import pprint
from typing import Annotated

from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi import Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.routers import url_crud
from ..database import get_db
from .url_schemas import UrlResponse, UrlCreate

router = APIRouter(prefix='/urls',
                   tags=['Urls API'])

templates = Jinja2Templates(directory="app/templates")


@router.get('/add-url', name='add_url', response_class=HTMLResponse)
async def show_new_url(r: Request):
    context = {'request': r}
    return templates.TemplateResponse('add-url.html', context)


@router.post('/generated-url', name='generated_url', response_class=HTMLResponse)
async def show_generated_url(r: Request,
                             db: Annotated[Session, Depends(get_db)],
                             full_url: str = Form()):
    context = {'request': r}
    new_url = get_new_url(db, full_url)
    context['short_url'] = f"{r.url.scheme}://{r.url.hostname}:{str(r.url.port)}/{new_url.short_url_path}"

    return templates.TemplateResponse('generated-url.html', context)


@router.post("/", response_model=UrlResponse)
def create_url(url: UrlCreate,
               db: Annotated[Session, Depends(get_db)],
               r: Request):
    new_url = get_new_url(db, url.full_url)
    new_url.short_url = f"{r.url.scheme}://{r.url.hostname}:{str(r.url.port)}/{new_url.short_url_path}"

    return new_url


def get_new_url(db: Session, url: str):
    number_of_attempts = 0
    while True:
        # try 100 times to get unique ID otherwise sorry
        if number_of_attempts >= 100:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail='Cannot generate short url. Try later')
        number_of_attempts += 1
        new_url = url_crud.create_url(db, url)
        if new_url is None:
            continue
        else:
            break
    return new_url
