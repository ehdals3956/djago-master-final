from django.urls import path
from .import views

app_name = "Service"

urlpatterns = [
    path('compute/', views.compute, name="compute"),
    path('database/', views.database, name="database"),
    path('security/', views.security, name="security"),
    path('network/', views.network, name="network"),
    path('storage/', views.storage, name="storage"),
]
