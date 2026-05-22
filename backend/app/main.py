from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.core.logger import setup_logging
from app.middleware import auth_middleware
from app.db import models
from app.db.session import engine
from app.db.base import Base

setup_logging()
Base.metadata.create_all(bind=engine.sync_engine)

app = FastAPI(
    title='RetailLink Platform API',
    description='RetailLink backend for marketplace, group buying, and retailer-fintech orchestration.',
    version='0.1.0',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.middleware('http')(auth_middleware)

app.include_router(api_router, prefix='/api/v1')

@app.get('/')
def root():
    return {'message': 'RetailLink API is running'}
