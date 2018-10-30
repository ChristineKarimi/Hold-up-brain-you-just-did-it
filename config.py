import os
import hashlib

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    ECRET_KEY = os.environ.get('SECRET_KEY', str(hashlib.sha512(b"19HKjoD9tobNvEqxHYIeWobYSxse").hexdigest()))
    SECRET_KEY=""
    FAKE_USERS_JSON_FILE=BASE_DIR+"/project_utils/fake_users.json"

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}