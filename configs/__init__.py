from decouple import AutoConfig
from pathlib import Path

path = Path(__file__).resolve().parent / 'local'
if not path.exists():
    path = Path(__file__).resolve().parent / 'test'
if not path.exists():
    path = Path(__file__).resolve().parent / 'prod'

config = AutoConfig(search_path=path)

# 以 sqlalchemy 为例
SQLALCHEMY_ENGINE_CONFIG = {
    'pool_size': config('SQLALCHEMY_POOL_SIZE', 10, cast=int),
    'max_overflow': config('SQLALCHEMY_MAX_OVERFLOW', 10, cast=int),
    'pool_timeout': config('SQLALCHEMY_POOL_TIMEOUT', 10, cast=int),
    'pool_pre_ping': config('SQLALCHEMY_POOL_PRE_PING', False, cast=bool),
    'echo': config('SQLALCHEMY_POOL_ECHO', False, cast=bool),
}
