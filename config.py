import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    MSEARCH_INDEX_NAME = 'whoosh_index'
    # simple,whoosh
    MSEARCH_BACKEND = 'whoosh'
    # auto create or update index
    MSEARCH_ENABLE = True
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    DB_DEFAULT_USER = 'gk_usr' # 'root'
    DB_DEFAULT_USER_PASS = 'testPass123'
    DB_DEFAULT_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'mysql://' + DB_DEFAULT_USER + ':' + DB_DEFAULT_USER_PASS + '@' + DB_DEFAULT_HOST + '/gksvcat_dev_db'

class TestingConfig(Config):
    TESTING = True
    DB_DEFAULT_USER = 'root'
    DB_DEFAULT_USER_PASS = ''
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'mysql://' + DB_DEFAULT_USER + '@' + DB_DEFAULT_USER_PASS + '/gksvcat_test_db'

class ProductionConfig(Config):
    DB_DEFAULT_USER = 'j980_gksv_usr'
    DB_DEFAULT_USER_PASS = 'aFm894FD'
    DB_DEFAULT_HOST = 'mysql.geekingdom.sv'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'mysql://' + DB_DEFAULT_USER + ':' + DB_DEFAULT_USER_PASS + '@' + DB_DEFAULT_HOST + '/gksvcat_db'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}