

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from jobapp.models import MyUser, EmployeerProfile,Job,ApplicationJob


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["first_name", "last_name", "username", "password1", "password2", "email", "mobile", "gender","usertype"]


        widgets={"usertype":forms.HiddenInput(attrs={"value":"Jobseeker"}),
            "first_name": forms.TextInput(attrs={"class": "form-control","placeholder":"First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "mobile": forms.TextInput(attrs={"class": "form-control", "placeholder": "Mobile Number"}),
            "gender": forms.TextInput(attrs={"class": "form-control", "placeholder": "Gender"}),
        }

class MyUserSigninForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter Password'}))


class EmployerCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["first_name", "last_name", "username", "password1", "password2", "email", "mobile", "gender",
                  "usertype"]
        widgets = {"usertype": forms.HiddenInput(attrs={"value": "Employer"}),
                   "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
                   "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
                   "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
                   "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
                   "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}),
                   "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
                   "mobile": forms.TextInput(attrs={"class": "form-control", "placeholder": "Mobile Number"}),
                   "gender": forms.TextInput(attrs={"class": "form-control", "placeholder": "Gender"}),
                   }
        # model = EmployeerProfile
        # fields = ["username", "password", "company_name", "address", "email", "phone", "contact_person"]



class EmployerSigninForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter Password'}))

class GetUserAccountMixin():
    def get_user_account(self,id):
        try:
            return  MyUser.objects.get(id=id)
        except:
            return None


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["job_title","job_details","status","phone","email","location","description","experience","last_date"]
        widgets = {"job_title": forms.TextInput(attrs={"class": "form-control", "placeholder": "JOB TITLE"}),
                   "job_details": forms.Textarea(attrs={"class": "form-control", "placeholder": "Details"}),
                   "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
                   "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
                   "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Location"}),
                   "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Description"}),
                   "experience": forms.TextInput(attrs={"class": "form-control", "placeholder": "Experience"}),
                   "last_date": forms.TextInput(attrs={"class": "form-control"})
                   }

class ApplyJobForm(forms.ModelForm):

    class Meta:
        model=ApplicationJob
        exclude = ['id', 'job_apply']
        fields=["name","phone","email","address","experience","qualifications","status"]
        widgets = {"status": forms.HiddenInput(attrs={"value": "Pending"}),
                   "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}),
                   "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
                   "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email ID"}),
                   "address": forms.Textarea(attrs={"class": "form-control", "placeholder": "Address"}),
                   "experience": forms.TextInput(attrs={"class": "form-control", "placeholder": "Experience"}),
                   "qualifications": forms.Textarea(attrs={"class": "form-control", "placeholder": "Qualifications"}),
                   }