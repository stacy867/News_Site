class Source:
    source= []
    '''
    news'source to define news_source objects
    '''
    
    def __init__(self,id,name,country,sourceurl):
        self.id = id
        self.name = name
        self.country = country
        self.sourceurl = sourceurl
        
class Article:
    articles= []
    '''
    news'article to define articles objects
    '''
    
    def __init__(self,author,tittle,imageurl,description,time):
        self.author = author
        self.tittle = tittle
        self.imageurl = imageurl
        self. description = description
        self.time = time 
        
    def save_articles(self):
        Article.articles.append(self)
        
        
    @classmethod
    def clear_articles(cls):
        Article.articles.clear() 
        
    @classmethod
    def get_articles(cls,author1):
        
        response = []
        
        for art in cls.articles:
            if article.author == author1:
                response.append(art)
        return response   
                   