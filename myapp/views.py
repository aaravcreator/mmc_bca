from django.shortcuts import render,redirect
from .models import Student,BloodRequest,ContactMessage
from .forms import StudentForm
# Create your views here.
def list_student_view(request):
    students = Student.objects.all()
    data = {
        'students':students
                }

    return render(request,"list_student.html",data)

def delete_student(request,id):
    student = Student.objects.get(id=id)

    student.delete()
    return redirect('/list_student/')

def update_student(request,id):
    print(id)
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/list_student/')
    data = {
        'form':form
    }

    return render(request,'update.html',data)


def create_student(request):

    print(request.POST)
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() # saves the student data to database
            return redirect('/list_student/')


    
    data = {
        'form':form
    }
    return render(request,"create_student.html",data)

def emergency_view(request):

    blood_requests = BloodRequest.objects.filter(is_expired=False,is_verified=True)
    data = {
        'blood_requests':blood_requests
    }



    return render(request,"emergency.html",data)

def contact_view(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_msg = ContactMessage()
        contact_msg.name = name
        contact_msg.email = email
        contact_msg.message = message
        contact_msg.save()
        return redirect('/contact/')



    return render(request,"contact.html")


