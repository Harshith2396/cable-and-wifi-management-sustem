"""cablewifi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cableadmin import views as v
from manager import views as v1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('deleteplan/',v.deleteplan,name='deleteplan'),
    path('userdelete',v.userdelete,name='userdelete'),
    path('userdetails',v.userdetails,name='userdetails'),
    path('updatearea',v.updatearea,name='updatearea'),
    path('getplan',v.getplan,name='getplan'),
    path('getinfo',v.getinfo,name='getinfo'),
    path('admindetails',v.admindetails,name='admindetails'),
    path("login",v.logins,name='login'),
    path('',v.homepage),
    path('managerlogin',v1.managerlogin,name='managerlogin'),
    path('userlogin',v.userlogin,name="userlogin"),
    path('logout',v.logouts,name='logout'),
    path('usercatalog',v.usercatalog,name='usercatalog'),
    path('useroptions',v.useroptions,name='useroptions'),
]
