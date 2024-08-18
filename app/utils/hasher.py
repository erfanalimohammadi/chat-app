from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from App.config.config import get_settings

settings = get_settings()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def verify_password(plain_password: str, hashed_password: str) -> bool:

    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    
    return pwd_context.hash(password)
