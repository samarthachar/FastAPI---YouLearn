from pydantic_settings import BaseSettings #type: ignore

class Settings(BaseSettings):
    app_name: str = "Test API"
    environment: str = "dev"

    secret_key: str = "change_me"
    access_token_expire_minutes: int = 60

    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()