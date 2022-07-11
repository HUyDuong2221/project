from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from  .forms import baivietform, thembaiviet
# Create your views here.

def home(request):
    bv = baiviet.objects.all()
    
    return render(request, 'home.html', {'baiviet':bv})

def them(request):
    form = thembaiviet()
    return render(request, 'them.html', {'f':form})

def save(request):
    if request.method == 'POST':
        f = thembaiviet(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse('luu ok')
        else:
            return HttpResponse('khong dung kieu du lieu')
    else:
        return HttpResponse('khong phair post')

    
def login(request):
    return render(request, 'login.html')