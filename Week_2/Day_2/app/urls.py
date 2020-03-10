from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('new_person', views.newPerson),
    path('new_pet', views.newPet)
]