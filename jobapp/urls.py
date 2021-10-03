from django.urls import path
from .views import MyUserCreateView, MyUserSigninView, MyUserHomeView, EmployerCreateView, EmpHomeView, UserSignoutView, \
    EmpSignoutView, AddJobView, ListJobView, UpdateJobView, DeleteJobView, ViewJobs, ViewApplications, ApplyJobView, \
    EmployerSigninView, SearchView,UpdateJobStatusView

from django.views.generic import TemplateView
urlpatterns=[
    path("ulogin",MyUserSigninView.as_view(),name="signin"),
    path("uregister",MyUserCreateView.as_view(),name="signup"),
    path("elogin",EmployerSigninView.as_view(),name="esignin"),
    path("eregister",EmployerCreateView.as_view(),name="esignup"),
    path("home",MyUserHomeView.as_view(),name="home"),
    path("ehome",EmpHomeView.as_view(),name="ehome"),
    path("usignout",UserSignoutView.as_view(),name="usignout"),
    path("esignout",EmpSignoutView.as_view(),name="esignout"),
    path("addjob", AddJobView.as_view(), name="postjob"),
    path("list", ListJobView.as_view(), name="list"),
    path("job/update/<int:pk>", UpdateJobView.as_view(), name="update"),
    path("job/delete/<int:pk>", DeleteJobView.as_view(), name="delete"),
    path("view",ViewJobs.as_view(),name="view"),
    path("job/viewappln/<int:pk>",ViewApplications.as_view(),name="viewappln"),
    path("job/apply/<int:pk>",ApplyJobView.as_view(),name="apply"),
    path("search",SearchView.as_view(),name="search"),
    path("job/edit/<int:pk>",UpdateJobStatusView.as_view(),name="edit")
]