from datetime import datetime, timedelta
from typing import Any
from fastapi import Depends
from jose import JWTError, jwt
from app.models import user as user_model


settings = get_settings()


# JWT settings
SECRET_KEY = settings.jwt_secret_key.get_secret_value()
ALGORITHM = settings.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
REFRESH_TOKEN_EXPIRE_DAYS = settings.refresh_token_expire_days


def create_token(
    data: dict[str, Any],
    token_type: str,
    expires_delta: timedelta | None = None,
) -> str:
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        match token_type:
            case "access":
                expire = datetime.now() + timedelta(
                    minutes=ACCESS_TOKEN_EXPIRE_MINUTES
                )
            case "refresh":
                expire = datetime.now() + timedelta(
                    days=REFRESH_TOKEN_EXPIRE_DAYS
                )
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def parse_token(token: str) -> dict[str, Any]:
    
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"verify_signature": False},
        )
        return payload
    except JWTError as e:
        logger.error(f"JWT error: {e}")  # Log the error for debugging purposes
        raise credentials_exception


def validate_token(token: str) -> bool:
  
    try:
        # Decode the token without validating the signature to check expiration
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"verify_signature": False},
        )
        # Check if the token is expired
        if (
            payload.get("exp")
            and datetime.fromtimestamp(payload["exp"]) < datetime.now()
        ):
            return False
        return True
    except JWTError as e:
        logger.error(f"JWT error: {e}")
        return False


async def get_current_user(
    token: str = Depends(hasher.oauth2_scheme),
) -> user_model.UserInDB:
    
    payload = parse_token(token)
    username: str | None = payload.get("username")

    if username is None:
        logger.error("Username is missing in the token payload.")
        raise credentials_exception

    user: user_model.UserInDB | None = await user_model.fetch_user_by_username(
        username
    )

    # Raise an exception if no user was found
    if user is None:
        logger.error(f"User with username {username} not found in database.")
        raise credentials_exception

    return user


async def authenticate_user(
    username: str, password: str
) -> user_model.UserInDB | None:
    user: user_model.UserInDB | None = await user_model.fetch_user_by_username(
        username
    )

    # Return None if no user was found or if password verification fails
    if user is None or not hasher.verify_password(
        password, user.hashed_password
    ):
        return None

    return user
