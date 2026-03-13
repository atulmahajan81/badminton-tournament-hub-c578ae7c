import os
from datetime import datetime, timedelta
from typing import Tuple
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseSettings, Field

# Configuration for JWT and bcrypt
class AuthSettings(BaseSettings):
    secret_key: str = Field(..., env='SECRET_KEY')  # Ensure this is set in environment
    algorithm: str = 'HS256'
    access_token_expire_minutes: int = 15
    refresh_token_expire_minutes: int = 1440  # 1 day

    class Config:
        env_file = '.env'

settings = AuthSettings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a password for storing."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.access_token_expire_minutes))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: timedelta = None) -> str:
    """Create a JWT refresh token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(days=1))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt