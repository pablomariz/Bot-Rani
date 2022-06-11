from tinydb import TinyDB

__db = TinyDB("persistent.json")


def get_db():
    return __db