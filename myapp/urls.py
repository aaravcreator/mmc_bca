from django.urls import path

from .views import *

urlpatterns = [
    path('list_student/',list_student_view),
    path('create/',create_student),
]