from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database import Base


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_url = Column(String, unique=True, index=True, nullable=False)
    full_url = Column(String, unique=False, index=True, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)