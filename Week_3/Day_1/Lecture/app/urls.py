from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('dog/new', views.create_dog), # create form
    path('dog/create', views.add_dog),
    path('dog/<int:id>/toggle_good_boy', views.toggle),
    path('dog/<int:id>/edit', views.edit), # edit form
    path('dog/<int:id>/update', views.update),
    path('dogs/<int:id>', views.one_dog),
    path('dog/<int:id>/delete', views.delete),
]