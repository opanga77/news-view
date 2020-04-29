import os


class Config:
    """Main configurations class"""

    NEWS_API_KEY = '34343a075fe6498787303b528b06ad33'
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/'
    # NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/{}?apiKey={}' // APPLIES WHEN THE base_url is passed as the string
    SECRET_KEY = 'U\x1f\xbd\xfb<\xfea\x0c\xf3a{\x06'



class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    pass


class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
