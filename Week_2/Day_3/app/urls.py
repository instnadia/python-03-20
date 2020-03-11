from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('add_student', views.add_s),
    path('teachers', views.display_teachers),
    path('add_teacher', views.add_t),
    path('student/<int:id>', views.show_s),
]