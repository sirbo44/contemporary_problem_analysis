from django.urls import path
from mapPage import views

urlpatterns = [
    path('', views.index ,name="index"),
]
