
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    mobile = models.CharField(max_length=12)
    option1 = (("male", "male"),
               ("female", "female")
               )
    gender = models.CharField(max_length=120, choices=option1, default="male")
    usertype=models.CharField(max_length=50,null=1)

class UserProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=120)
    skills = models.CharField(max_length=120)
    experience = models.CharField(max_length=120)



class EmployeerProfile(models.Model):
    username= models.CharField(max_length=120,null=0,default="employer")
    password = models.CharField(max_length=120, null=0, default="employer")
    company_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=12,null=1)
    email = models.CharField(max_length=100,null=1)
    contact_person = models.CharField(max_length=100,default="HR")

class Job(models.Model):
    job_title = models.CharField(max_length=40)
    #employeer = models.ForeignKey(EmployeerProfile, on_delete=models.CASCADE)
    job_details = models.CharField(max_length=120)
    options = (("active", "active"),
               ("closed", "closed"))
    status = models.CharField(max_length=120, choices=options, default="active")
    phone = models.CharField(max_length=12,null=1)
    email = models.CharField(max_length=100,null=1)
    location = models.CharField(max_length=120,null=1)
    description = models.CharField(max_length=120,null=1)
    experience = models.CharField(max_length=120,null=1)
    image=models.ImageField(null=1)
    date_created = models.DateField(auto_now=True)
    last_date = models.DateField(max_length=120,null=1)




class ApplicationJob(models.Model):
    id=models.AutoField(primary_key=True)
    job_apply = models.ForeignKey(Job, on_delete=models.CASCADE)
    # jobseeker_id = models.IntegerField()
    name = models.CharField(max_length=120, null=1)
    phone = models.CharField(max_length=12, null=1)
    email = models.CharField(max_length=100, null=1)
    address = models.CharField(max_length=500, null=1)
    experience = models.CharField(max_length=120, null=1)
    qualifications= models.CharField(max_length=120, null=1)
    applied_date = models.DateField(auto_now=True)
    options = (("Pending", "Pending"),
               ("Accept", "Accept"),
               ("Reject", "Reject"),
               ("Approve", "Approve")
               )
    status = models.CharField(max_length=120, choices=options, default="Pending")




