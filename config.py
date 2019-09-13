import os

class Config:
    NEWS_ARTICLE_BASE_URL ='https://newsapi.org/v2/{}?q=bitcoin&from=2019-08-13&sortBy=publishedAt&apiKey={}'
    NEWS_SOURCE_BASE_URL='https://newsapi.org/v2/sources{}?apiKey={}'
    NEWS_ARTICLE_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(config):
    pass


class DevConfig(config):
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}        