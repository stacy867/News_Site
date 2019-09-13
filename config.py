import os

class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?q=bitcoin&from=2019-08-13&sortBy=publishedAt&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(config):
    pass


class DevConfig(config):
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}        