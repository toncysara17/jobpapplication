from django.http import request
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView,ListView,UpdateView,DeleteView,DetailView

from .forms import MyUserCreationForm, MyUserSigninForm, EmployerCreationForm,EmployerSigninForm,JobForm,ApplyJobForm
from .models import MyUser, EmployeerProfile,Job,ApplicationJob
from .decorators import loginrequired

# Create your views here.
class MyUserCreateView(CreateView):
    model = MyUser
    form_class = MyUserCreationForm
    template_name = "userregistration.html"
    success_url = reverse_lazy("signin")

class MyUserHomeView(ListView):
    model = Job
    template_name = "userhome.html"
    context_object_name ="jobslist"

class EmpHomeView(ListView):
    model = Job
    template_name = "emphome.html"
    context_object_name = "jobslist"


class ListJobView(ListView):
    model = Job
    template_name = "listjob.html"
    context_object_name ="jobslist"

class MyUserSigninView(TemplateView):
    model = MyUser
    form_class = MyUserSigninForm
    template_name = "userlogin.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usertype = 'Jobseeker'
            user = authenticate(request, username=username, password=password, usertype=usertype)
            #user = authenticate(request, username=username, password=password)
            if user:
                print("success")
                login(request, user)
                return redirect("home")
            else:
                print("fail")
            return render(request, self.template_name, self.context)

class UserSignoutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return  redirect("signin")

class EmployerCreateView(CreateView):
    model = MyUser
    form_class = EmployerCreationForm
    template_name = "empregistration.html"
    success_url = reverse_lazy("esignin")



class EmployerSigninView(TemplateView):
    model = MyUser
    form_class =EmployerSigninForm
    template_name = "emplogin.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usertype='Employer'
            user = authenticate(request, username=username, password=password, usertype=usertype)
            if user:
                print("success")
                login(request, user)
                return redirect("ehome")
            else:
                print("fail")
                return render(request, self.template_name, self.context)

class EmpSignoutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return  redirect("esignin")

class AddJobView(CreateView):
    model = Job
    form_class = JobForm
    template_name = "postnewjob.html"
    success_url = reverse_lazy("postjob")

class UpdateJobView(UpdateView):
    model = Job
    template_name = "updateJob.html"
    form_class = JobForm
    success_url = reverse_lazy("list")

class DeleteJobView(DeleteView):
    model = Job
    template_name = "delete.html"
    success_url = reverse_lazy("list")

class ViewJobs(DetailView):
    model = Job
    template_name = "viewjob.html"
    context_object_name = "jobs"

class ViewApplications(ListView):
    model = ApplicationJob
    template_name = "viewapplictions.html"
    #context_object_name = "jobslist"

    def get_queryset(self):
        return ApplicationJob.objects.filter( job_apply=self.kwargs['pk'])

class GetObjectMixin:
    def get_context_data(self, **kwargs):
        id = self.kwargs['pk']
        return id
    def get_object(self, id):
        return self.model.objects.get(id=id)


class ApplyJobView(CreateView,GetObjectMixin):
    model = ApplicationJob
    form_class = ApplyJobForm
    template_name = "applyjob.html"
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.job_apply = Job.objects.get(id=self.kwargs['pk'])
            recipe.save()
            return redirect("home")
class SearchView(ListView):
    model = Job
    template_name = 'userhome.html'
    context_object_name = 'jobslist'

class UpdateJobStatusView(UpdateView):
    model = ApplicationJob
    template_name = "updatejobstatus.html"
    form_class = ApplyJobForm
    success_url = reverse_lazy("list")
