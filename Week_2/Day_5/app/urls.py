from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.reg),
    path('success', views.success),
    path('login', views.log),
    path('logout', views.logout),
]