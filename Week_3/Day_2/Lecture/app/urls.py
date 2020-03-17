from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.reg),
    path('success', views.success), # message form here
    path('login', views.log),
    path('logout', views.logout),
    path('addMessage', views.new_message),
    path('addComment/<int:id>', views.new_comment), #add a comment with a unique id that relates to the message that comment is posted on
]