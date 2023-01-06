import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('Utilities/properties.ini')
    return config
