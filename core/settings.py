from pydantic_settings import BaseSettings

#configs do banco de dados:
user = "postgres"
password = "Junior32720131%"
host = "localhost"
port = "5432"
DB = "faculdade"


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{DB}"

    class Config:
        case_sensitive = True

settings: Settings = Settings()