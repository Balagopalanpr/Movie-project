from django.shortcuts import render
from Movies.models import Movie
from Movies.form import Movieform

# Create your views here.
def home(request):
    m=Movie.objects.all()
    return render(request,'home.html',{'m':m})

def add(request):
    if(request.method=="POST"):
        n=request.POST['n']
        y=request.POST['y']
        d=request.POST['d']
        i=request.FILES['i']
        m=Movie.objects.create(name=n,year=y,desc=d,image=i)
        m.save()
        return home(request)
    return render(request,'add.html')

def details(request,n):
    m=Movie.objects.get(id=n)
    return render(request,'details.html',{'m':m})

def delete(request,n):
    m=Movie.objects.get(id=n)
    m.delete()
    return home(request)

def update(request,n):
    m=Movie.objects.get(id=n)
    if(request.method=="POST"):
        form=Movieform(request.POST,request.FILES,instance=m)
        if form.is_valid():
            form.save()
            return home(request)
    form=Movieform(instance=m)
    return render(request,'update.html',{'form':form})
