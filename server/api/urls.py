from django.urls import path
from . import views

urlpatterns = [
    path("v1/", views.API.as_view(), name = "api")
]