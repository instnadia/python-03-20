from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),
    path('hello', views.hello),
    path('hello/<str:name>', views.hello_with_name),
    path('html', views.returnHTML),
]