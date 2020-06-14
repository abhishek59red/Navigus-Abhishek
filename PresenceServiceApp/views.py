from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


from .forms import UserRegistration
from .models import Profile
# Create your views here.
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('panel')
    else:
        
        if request.method == "POST" and request.FILES['myfile']:
           
            username = request.POST.get("username")
            email = request.POST.get("email")
            pass1 = request.POST.get("pass1")
            pass2 = request.POST.get("pass2")
            photo = request.FILES['myfile'] 
            is_user = User.objects.filter(username=username)
            if len(is_user) > 0:
                msg = "username already taken"
                return render(request, 'index.html', {'msg':msg})
            
            if len(photo) is None:
                msg = "please select image"
                return render(request, 'index.html', {'msg':msg})

            if pass1 != pass2 :
                msg = "Your Password does not Match"
                return render(request, 'index.html', {'msg':msg})
            
            prof = Profile(user = username ,pic = photo)
            prof.save()
            user = User.objects.create_user(username=username, email=email, password=pass1)
            user.save
            print("success")
            
            
    return render(request, "index.html")

def home(request):
    msg = ""
    if request.user.is_authenticated:
        return redirect('panel')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username= username, password=password)
            
            if user is not None:
                login(request, user)
                u = User()
                prosta = Profile.objects.filter(user=username)
                
                if len(prosta) > 0:
                    pro = Profile.objects.get(user = username)
                    pro.status = True
                    pro.save()
                else:
                    pro = Profile(user = username,status=True )
                    pro.save()
                return redirect('panel')
            else:
                msg = "401 - Unauthorized Access"
                return render(request, 'error.html' , {'msg':msg})
    return render(request, 'index.html' )


def logoutUser(request):
    pro = Profile.objects.get(user = request.user)
    pro.status = False
    pro.save()
    logout(request)
    return redirect("/")



@login_required(login_url='home')
def panel(request):
    users = Profile.objects.all()
    return render(request, 'panel.html', {'list':users,'media_url':settings.MEDIA_URL})

