class AppConfig:
    DB: str
    logging = "test"

    def __init__(self):
        print("In AppConfig constructor")


class DevConfig(AppConfig):
    DB = "dev"

    def __init__(self):
        print(" InDevConfig")


class StagingConfig(AppConfig):
    DB = "staging"

    def __init__(self):
        print("In StagingConfig")


class ProdConfig(AppConfig):
    DB = "prod"

    def __init__(self):
        print("In ProdConfig")
