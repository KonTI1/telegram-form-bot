import pathlib

from pydantic_settings import BaseSettings

def get_path_env() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent.parent / ".env"

class Settings(BaseSettings):
    bot_token: str
    ADMIN_ID: list[int]

    class Config:
        env_file = get_path_env()
        env_file_encoding = "utf-8"
        case_sensitive = False

    def get_db_url(self) -> str:
        db_path = pathlib.Path(__file__).resolve().parent.parent / "db" / "base.db"
        return db_path
    
settings = Settings()