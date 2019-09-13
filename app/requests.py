import urllib.request,json
from .models import Source
from .models import Article

#Getting api key
api_key = None
#Getting the news base url
articles_url = None
source_url = None

def configure_request(app):
    global api_key,articles_url,source_url
    api_key = app.config['NEWS_API_KEY']
    articles_url = app.config['NEWS_ARTICLE_BASE_URL']
    source_url = app.config['NEWS_SOURCE_BASE_URL']