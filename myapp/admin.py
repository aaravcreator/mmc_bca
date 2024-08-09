from django.contrib import admin

from myapp.models import Student,Customer,BloodRequest,ContactMessage

admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(BloodRequest)
admin.site.register(ContactMessage)


# Register your models here.
