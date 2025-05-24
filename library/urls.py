# library/urls.py
from django.urls import path

from concerts.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
