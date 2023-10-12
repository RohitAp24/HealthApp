from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from .forms import AppointmentForm
from .forms import CustomerLoginForm
from django.contrib import messages
from django.contrib.auth.models import User, AbstractUser




# Create your views here.
def index(request):
    return render(request, 'index1234.html')


def registration(request):
    return render(request,'reg.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login.html')  
    else:
        form = UserRegistrationForm()
    return render(request, 'reg.html', {'form': form})


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')        
    
            
          
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chome.html')  
        
        else:
            error_message = 'Invalid username or password'
            messages.error(request, error_message)  
            return redirect('login.html')  
    
    else:
        form = CustomerLoginForm
        return render(request, 'login.html', {'form':form})
    

def chome(request):
    return render(request,'chome.html')