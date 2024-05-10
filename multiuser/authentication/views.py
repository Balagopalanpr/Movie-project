from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from authentication.models import CustomUser
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def adminhome(request):
    return render(request,'adminhome.html')
def teacherhome(request):
    return render(request,'teacherhome.html')
def studenthome(request):
    return render(request,'studenthome.html')

def adminsignup(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        if (cp == p):
            user = CustomUser.objects.create_user(username=u, password=p, email=e, phone=n, address=a)
            user.is_superuser=True
            user.save()
            return home(request)
        else:
            return HttpResponse("passwords are not same")
    return render(request,'admin.html')

def studentsignup(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        if (cp == p):
            b = CustomUser.objects.create_user(username=u, password=p, email=e, phone=n, address=a)
            b.is_student = True
            b.save()
            return home(request)
        else:
            return HttpResponse("passwords are not same")
    return render(request,'students.html')

def teachersignup(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        n = request.POST['n']
        a = request.POST['a']
        if (cp == p):
            u = CustomUser.objects.create_user(username=u, password=p, email=e, phone=n, address=a)
            u.is_teacher=True
            u.save()
            return home(request)
        else:
            return HttpResponse("passwords are not same")
    return render(request,'teacher.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user and user.is_superuser==True:
            login(request,user)
            return adminhome(request)
        elif user and user.is_teacher==True:
            login(request,user)
            return teacherhome(request)
        elif user and user.is_student==True:
            login(request,user)
            return studenthome(request)
        else:
            return HttpResponse("invalid Credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return home(request)