from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from app_name.views.pages import PageView


urlpatterns = [
    re_path(r'^.*$', PageView.as_view(), name='index')
]
