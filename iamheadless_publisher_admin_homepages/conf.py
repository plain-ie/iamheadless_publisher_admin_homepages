from django.conf import settings as dj_settings

from .apps import IamheadlessPublisherAdminHomepagesConfig as AppConfig


class Settings:

    APP_NAME = AppConfig.name
    ITEM_TYPE = 'homepage'

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
