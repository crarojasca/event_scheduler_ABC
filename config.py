class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////db/local.db'
    SECRET_KEY = 'secret-key-goes-here'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    ECRET_KEY = 'secret-key-goes-here'