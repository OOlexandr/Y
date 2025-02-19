from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: int
    postgres_domain: str
    postgres_port: int
    postgres_db_name: str
    postgres_path: str

    class Config:
        env_file = Path(__file__).parent.joinpath(".env")
        env_file_encoding = "utf-8"


settings = Settings()
print(settings.Config.env_file)