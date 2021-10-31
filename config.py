


class Config():
    SQLALCHEMY_DATABASE_URL = "sqlite:///app.db"


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URL = "sqlite:///app.db"

