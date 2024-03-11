import configparser


from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from dataclasses import dataclass
from typing import List

# allowed_ids: List[int] = [1585242629]


@dataclass
class BotToken:
    token: str
    admin_id: set[int]


@dataclass
class Database:
    port: int
    host: str
    database_name: str
    database_user: str
    password: str


# @dataclass
# class TimingDelta:
#     time_raise_asyncio_ban: int
#     minute_delta: int
#     time_raise_asyncio_del_msg: int


@dataclass
class Config:
    tg_bot: BotToken
    db: Database
    # time_delta: TimingDelta


def load_config(path):
    config = configparser.ConfigParser()
    config.read(path)

    token = config['tg_bot']
    database = config['db']
    # time = config['timedelta']

    return Config(
        tg_bot=BotToken(
            token=token.get('token'),
            admin_id=token.get('admin_id')),

        db=Database(
            database_name=database.get('POSTGRES_DB'),
            database_user=database.get('POSTGRES_USER'),
            port=database.get('POSTGRES_PORT'),
            host=database.get('POSTGRES_HOST'),
            password=database.get('POSTGRES_PASSWORD')),
            
        # time_delta=TimingDelta(
        #     time_raise_asyncio_ban=time.get('TIME_RAISE_ASYNCIO_BAN'),
        #     minute_delta=time.get('TIME_ONE_MINUTE'),
        #     time_raise_asyncio_del_msg=time.get('TIME_RAISE_ASYNCIO_DEL_MSG'),
        )


config = load_config('config.ini')
DATABASE_url_async = (f'postgresql+asyncpg://{config.db.database_user}:{config.db.password}'
                      f'@{config.db.host}:{config.db.port}/{config.db.database_name}')
async_engine = create_async_engine(url=DATABASE_url_async, echo=True)
async_session = async_sessionmaker(async_engine)
