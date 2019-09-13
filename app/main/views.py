from flask import render_template,request,redirect,url_for
from . import main
from ..models import Article
from ..models import Source
from app import app

#Views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and it's data
    '''
    title ='Welcome to the news website,fetch everykind of news from here'
    return render_template('index.html', title = title)

@main.route('/source/<int:source_id>')
def source(source_id):
    '''
    view source page function that returns the articles source
    '''
    return render_template('source.html',id = source_id)
