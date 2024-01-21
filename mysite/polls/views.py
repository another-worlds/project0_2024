from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post, Comment
from random import randint


# Create your views here.
def index(request):
    # Get Post list as a dictionary argument
    args = { "posts" : Post.objects.order_by("-pub_date")[:5] }
    
    # Construct template via loader
    template = loader.get_template("polls/index.html")
    
    # Render template and return as HttpRequest
    return HttpResponse(template.render(args, request))

def details(request, post_id):
    # Get post by post id
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all()[:5]
    args = { "post": post, "comments": comments}
    
    # Construct template via loader
    template = loader.get_template("polls/details.html")
    
    # Render template
    return HttpResponse(template.render(args, request))

def random_post(request):
    
    i = randint(1, Post.objects.count())
    post = Post.objects.get(pk=i)
    args = {"post" : post}
    
    template = loader.get_template('polls/details.html')
    return HttpResponse(template.render(args, request))
    

def about(request):
    args = {}
    template = loader.get_template("polls/about.html")
    return HttpResponse(template.render(args, request))