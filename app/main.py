from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from App.config.config import get_settings
from App.config.database import init_mongo_db, shutdown_mongo_db
from App.middlewares.request_limit import RequestLimitMiddleware
from App.routes import auth, chat, user
from App.sockets import sio_app


settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    
    await init_mongo_db(test_db=settings.test_mode)
    try:
        yield
    finally:
        await shutdown_mongo_db()


app = FastAPI(
    title="FastAPI Chat App",
    description="A chat application built with FastAPI and socket.io",
    version="1.0.0",
    lifespan=lifespan,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
)
app.add_middleware(RequestLimitMiddleware, max_requests=10, window_seconds=1)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.trusted_hosts,
)


app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(user.router, prefix="/user", tags=["user"])


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to the FastAPI Chat App"}



app.mount("/socket.io/", app=sio_app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
