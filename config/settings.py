from pydantic import BaseSettings
import datetime


class ServerSettings(BaseSettings):
    SECRET_KEY: str = "0f24ebaa5d85c370497c4780db4e1072d93c5d4f28c56642a4aa18e2d1eec363d63ab6f23bc16b3f"
    HOST: str = '0.0.0.0'
    PORT: int = 8000
    DEBUG: bool = True
    RELOAD: bool = True


class DatabaseSettings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: str = "5432"
    DB_NAME: str = "authdb"
    DB_USER: str = "sangram"
    DB_PASSWORD: str = "root"


class JwtTokenSettings(BaseSettings):
    EXPIRATION_TIME = datetime.timedelta(days=1,hours=0,minutes=0,seconds=0)


class CombinedSettings(ServerSettings,DatabaseSettings,JwtTokenSettings):...


settings = CombinedSettings()