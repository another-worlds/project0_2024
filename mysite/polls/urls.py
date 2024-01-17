from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('posts/<int:post_id>', views.details, name='details_url'),
    path('about', views.about, name='about_url')
]
