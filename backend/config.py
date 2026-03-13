from pydantic import BaseSettings, Field, ValidationError

class Settings(BaseSettings):
    """Application settings sourced from environment variables."""
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    DATABASE_URL: str = Field(..., env='DATABASE_URL')

    class Config:
        env_file = '.env'

try:
    settings = Settings()
except ValidationError as e:
    raise RuntimeError("Configuration error: Ensure all environment variables are set.") from e