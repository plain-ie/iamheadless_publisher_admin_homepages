from .apps import IamheadlessPublisherHomepagesTopicConfig


class Settings:

    APP_NAME = IamheadlessPublisherHomepagesTopicConfig.name
    ITEM_TYPE = 'homepage'

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
