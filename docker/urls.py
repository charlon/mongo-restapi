from django.urls import re_path, include
urlpatterns = [
    re_path(r'^', include('mongo_rest.urls'))
]
