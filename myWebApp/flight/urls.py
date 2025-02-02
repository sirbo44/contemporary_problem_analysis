from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='home'),
    path('api', views.api, name='api'),
]