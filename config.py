import configparser


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Config:
    def __init__(self, path):
        config = configparser.ConfigParser(interpolation=None)
        config.optionxform = str
        config.sections()
        config.read(path)

        self.tw = Struct(**dict(config["TW"]))
        self.app = Struct(**dict(config["APP"]))
