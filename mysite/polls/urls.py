from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index_url'),
    path('posts/<int:post_id>', views.details, name='details_url'),
    path('about', views.about, name='about_url')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
