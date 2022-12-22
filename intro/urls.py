from django.urls import path
from . import views

app_name = "intro"

urlpatterns = [

    path("index/", views.index, name="index"),
    path("page/", views.page, name="page"),


]