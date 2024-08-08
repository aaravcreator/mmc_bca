from django.urls import path

from .views import *

urlpatterns = [
    path('list_student/',list_student_view),
    path('create/',create_student),
    path('update/<int:id>/',update_student),
    path('delete/<int:id>/',delete_student),
    #localhost:8000/update/1/
]