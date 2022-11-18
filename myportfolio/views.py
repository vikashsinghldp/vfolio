from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Client

# Create your views here.
def index(request):
    return render(request,'index.html')
def addrecord(request):
    name=request.POST['Name']
    email=request.POST['Email']
    contact=request.POST['Contact']
    message=request.POST['Message']
    client=Client(name=name,email=email,contact=contact,message=message)
    client.save()
    return HttpResponseRedirect(reverse('index'))