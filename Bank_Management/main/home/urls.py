from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Home",views.index, name='home'),
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='Services'),
    path("contact",views.contactus, name='contactus'),
    path("User_Login",views.Userlogin, name='User_Login'),
    path("SignUp",views.SignUp, name='SignUp'),
    path("UserFrame",views.UserFrame, name='UserFrame'),
    path("trial",views.trial, name='trial'),
    path("logout",views.logout, name='logout')
]
