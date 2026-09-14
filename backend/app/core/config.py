from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    APP_NAME: str = "VETOR0"
    APP_TAGLINE: str = "Segurança Ofensiva para OT & SCADA"
    DEBUG: bool = True
    DATA_DIR: Path = BASE_DIR / "data"
    STATIC_DIR: Path = BASE_DIR / "frontend" / "static"
    TEMPLATES_DIR: Path = BASE_DIR / "frontend" / "templates"


settings = Settings()
