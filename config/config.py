from dataclasses import dataclass
from environs import Env


# Импорт данных из env-файла
@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('TOKEN')))


# Состояние игры и необходимые данные
state: dict = {
}
user_move: dict = {}
bot_move: dict = {}
likes_count: dict = {}

