from dataclasses import dataclass
from environs import Env
from typing import Optional, List

@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: List[int]

@dataclass
class LogSettings:
    level: str
    format: str


@dataclass
class Config:
    bot: TgBot
    log: LogSettings


def load_config(path: Optional[str] = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot=TgBot(token=env("BOT_TOKEN"), admin_ids=list(map(int, env.list('ADMIN_IDS')))),
        log=LogSettings(level=env("LOG_LEVEL"), format=env("LOG_FORMAT")),
    )