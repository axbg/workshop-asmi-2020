import yaml

from functools import lru_cache


@lru_cache
def load_vars():
    with open("config.yaml", "r") as config_file:
        vars = yaml.load(config_file, Loader=yaml.FullLoader)

    return vars
