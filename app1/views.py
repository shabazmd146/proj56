from django.shortcuts import render
from multiprocessing import context
from app1.models import car
from app1.forms import cars
from django.http import HttpResponseRedirect

# Create your views here.

def  index(request):
    context = {'msg':'this is index page'}
    return render(request,'app1/index.html',context)

def create(request):
    form = cars()
    if request.method == 'POST':
        form = cars(request.POST)
        if form.is_valid():
            form.save()
            form = cars()
        else:
            print('invalid formcourse')
    context = {'msg':'this is create page','form':form}
    return render (request,'app1/index.html',context)

def retrieve(request):
    Car = car.objects.all()
    context = {'msg':'This is the retrieve page','Car':Car}
    return render(request,'app1/index.html',context)

def update(request,id):
    if request.method == 'POST':
        Shabaz = car.objects.get(pk=id)
        form = cars(request.POST,instance=Shabaz)
        if form.is_valid():
            form.save()
            form = cars()
    else:
        Shabaz = car.objects.get(pk=id)
        form = cars(instance=Shabaz)
    a = {'msg':'This is update page','form':form}
    return render(request,'app1/update.html',a)

def delete(request,id):
    if request.method == 'POST':
        Shabaz = car.objects.get(pk=id)
        Shabaz.delete()
        return HttpResponseRedirect('/app1/retrieve')
        


