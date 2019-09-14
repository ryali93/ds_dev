from django.conf.urls import url, include
from django.contrib import admin

from blog.views import blog_index, blog_category, blog_detail

urlpatterns = [
	url(r'^$', blog_index, name="blog_index"),
	url(r'^(?P<pk>[0-9]+)$', blog_detail, name="blog_detail"),
	url(r'^(?P<category>\w+)$', blog_category, name="blog_category"),
]
