from django.shortcuts import render, redirect
from requests import post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login
from django.contrib.auth.forms import UserCreationForm
from .models import Feedback
import uuid
from django.conf import settings
from django.core.mail import send_mail
import urllib.request
import json



def article(request):
    return render(request,'article.html')



def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        third = Feedback(name=name,email=email,text=text)
        third.save()
        messages.success(request,'Thanks, Your Feedback has been submitted ! Our Mods will contact you soon ')
    return render(request,'feedback.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        User1 = authenticate(username=username,password=password)
        if User1 is not None:
            login(request,User1)
            return render(request,"group.html")
        else:
            return render(request,'login.html')
    return render(request,"login.html")

def logoutUser(request):
    logout(request)
    return redirect("/")


def RegisterUser(request):
        if request.method=="POST":
            try:
                username = request.POST.get("username")
                email = request.POST.get("email")
                password = request.POST.get("password")
                password2 = request.POST.get("password2")
                if len(password) >=8 and password != password2:
                        messages.error(request,"Passwords didn't match")
                elif len(password)>=8 and password==password2:
                    User.objects.create_user(username=username,email=email,password=password)
                    send_mail(subject=" Welcome To Vayu Plus !",message=f" Hey {username} Welcome to Vayu Plus The Perfect Place to know your day, Have Fun :) \n \n Team Vayu - Aryan, Vansh, Uday  ",from_email = settings.EMAIL_HOST_USER, recipient_list = [email] )
                    return redirect("/loginUser")
                else:
                    messages.error(request,"password is too short")
            except:
                messages.error(request,"Username already exists, try another")
        return render (request,"register.html")
    



def group(request):
    if request.user.is_anonymous:
        return redirect("/loginUser")
    return render(request,"group.html")


def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=01cca847017fc29a75ac3d80ac056717').read()
        list_of_data = json.loads(source)

        data = {
            "state":str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "index.html", data)
