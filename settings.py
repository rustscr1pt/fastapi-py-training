from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GOOGLE_TOKEN_ID : str = 'GOOGLE_TOKEN_ID'