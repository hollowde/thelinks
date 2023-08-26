from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from api import api_router

from wagtail import urls as wagtail_urls

urlpatterns = [


    path('api/v2/', api_router.urls),


    # Ensure that the api_router line appears above the default Wagtail page serving route
    re_path(r'^', include(wagtail_urls)),
]