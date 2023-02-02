from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Place
from .models import Traveller

# Create your views here..
def demo(request):
    obj=Place.objects.all()
    obj2=Traveller.objects.all()
    return render(request,"index.html",locals())







