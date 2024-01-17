from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post, Comment


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

def about(request):
    return HttpResponse("Nothing to see here(yet)")