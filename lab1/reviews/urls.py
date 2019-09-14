from django.conf.urls import url, include
from django.contrib import admin

from . views import index, list_review, add_review

urlpatterns = [
	url('^$', index, name='index'),
	url('list/', list_review, name='list_review'),
	url('add/', add_review, name='add_review')
]
