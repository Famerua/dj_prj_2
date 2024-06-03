from django.urls import path
from .views import get_index, get_about

urlpatterns = [
    path("", get_index),
    path("about", get_about)
    ]
