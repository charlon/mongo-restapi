from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from mongo_rest.views.pages import PageView
from mongo_rest.views.api import SpotAPIView


urlpatterns = [
    re_path(r'^api/spots', SpotAPIView.as_view()),
    re_path(r'^.*$', PageView.as_view(), name='index')
]
