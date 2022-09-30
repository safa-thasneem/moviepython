from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import movie
from .forms import movieform

# Create your views here.
def index(request):
    movie1=movie.objects.all()
    return render(request,"index.html",{'movie_list':movie1})

def details(request,movie_id):
    movie2=movie.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie2})

def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        image = request.FILES['image']
        movies=movie(name=name,desc=desc,year=year,image=image)
        movies.save()
    return render(request,'add.html')

def update(request,id):
    movies=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movies})

def delete(request,id):
    if request.method=='POST':
        movies=movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')