from django.conf.urls import include, url
from django.contrib import admin

from .views import oxford, github, github_client

urlpatterns = [
    url(r'oxford/', oxford, name='oxford'),
    url(r'github/', github, name='github'),
    url(r'github2/', github_client, name='github_client'),

]
