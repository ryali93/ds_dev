from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^process/$', views.process_cv, name='process_cv'),
	url(r'^cv/$', views.list_cv, name='list_cv'),
	url(r'^cv/(?P<cv_id>\d+)/$', views.cv_specific, name='cv_specific'),
]