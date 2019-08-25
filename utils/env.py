import os

from environs import Env

env = Env()
env.read_env(path="./.env")


def env(key, *, default=None):
    if key not in os.environ:
        return default
    return os.environ[key]
