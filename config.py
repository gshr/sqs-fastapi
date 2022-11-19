from pydantic import BaseSettings


class Settings(BaseSettings):
    aws_access_key: str
    aws_secret_key: str
    region_name :str

    class Config:
        env_file = '.env'


setting = Settings()
