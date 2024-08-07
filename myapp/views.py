from django.shortcuts import render
from .models import Student
from .forms import StudentForm
# Create your views here.
def list_student_view(request):
    students = Student.objects.all()
    data = {
        'students':students
                }

    return render(request,"list_student.html",data)

def create_student(request):

    print(request.POST)
    form = StudentForm()
    data = {
        'form':form
    }
    return render(request,"create_student.html",data)