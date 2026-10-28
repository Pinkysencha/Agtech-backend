from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All config comes from the .env file. Nothing secret is hard-coded."""
    port: int = 5000
    database_url: str
    jwt_secret: str
    ceda_api_key: str = ""
    frontend_url: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
