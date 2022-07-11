from email import message
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views import View
from django.http import *

# Create your views here.
class dangky(View):
    def get(self,request):
        dk = formdangky()
        return render(request, 'dangky.html', {'dk':dk})
    
    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username,email,password)
        user.save()
        return HttpResponse('dangky thanh cong')
    
class dangnhap(View):
    def get(self,request):
        dn= formdangky()
        return render(request, 'login.html',{'dn':dn})
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html')
def logout(request):
    logout()
    return HttpResponse('đã đăng xuất')