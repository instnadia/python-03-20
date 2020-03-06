from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('passLength', views.passLength),
    path('success', views.success)
]