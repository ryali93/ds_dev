from django.contrib import admin
from django.urls import include, path, re_path

from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="POLLS API")

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    #path("polls/", polls_list, name="polls_list"),
    #path("polls/<int:pk>/", polls_detail, name="polls_detail"),
    path("swaggerdocs/", schema_view),

]
