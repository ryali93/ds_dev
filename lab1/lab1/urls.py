from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url('', include('reviews.urls')),
    url(r'^admin/', admin.site.urls),
]
