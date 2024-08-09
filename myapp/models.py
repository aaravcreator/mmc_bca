from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    secondary_phone = models.CharField(max_length=10,null=True)

class BloodRequest(models.Model):
    bloodchoices = (
        ('A+', 'A+'),
        ('A-','A-'),
        ('B+', 'B+'),
        ('B-','B-'),
        ('AB+', 'AB+'),
        ('AB-','AB-'),
        ('O+', 'O+'),
        ('O-','O-'),
    )
    title = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=20,choices=bloodchoices)
    patient_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    requirement_date = models.DateField(null=True,blank=True)
    requirement_reason = models.CharField(max_length=100)
    is_expired = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    


