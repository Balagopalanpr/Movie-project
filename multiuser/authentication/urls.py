"""
URL configuration for multiuser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Function views
Examples:
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
from authentication import views
app_name="authentication"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('studentsignup/',views.studentsignup,name="student"),
    path('adminsignup/',views.adminsignup,name="admin"),
    path('teachersignup/',views.teachersignup,name="teacher"),
    path('user_login/',views.user_login,name="login"),
    path('user_logout/', views.user_logout, name="logout"),
    path('adminhome/',views.adminhome,name="adminhome"),
    path('teacherhome/',views.teacherhome,name="teacherhome"),
    path('studenthome/',views.studenthome,name="studenthome"),


]
