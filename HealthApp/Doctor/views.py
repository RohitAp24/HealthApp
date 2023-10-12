from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django. contrib import messages
from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm
from .forms import AvailabilityForm
from .forms import DoctorLoginForm
from .models import Doctor
import psycopg2

 


def dlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            conn = psycopg2.connect(
                host="localhost",
                user="postgres",
                password="1234",
                database="customer"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT username, password FROM doctor_table WHERE username = %s AND is_active = TRUE", [username])
            row = cursor.fetchone()
            print(row)
            if row is not None:
                db_username, db_password = row
                if password == db_password:
                    user = authenticate(request, username=db_username, password=db_password)
                    print (user)
                    if user is not None:
                        login(request, user)
                        return redirect(request, 'reg.html')
                    else:
                        messages.error(request, 'Authentication failed.')
                else:
                    messages.error(request, 'Invalid password.')
            else:
                messages.error(request, 'Invalid username.')
        except (psycopg2.Error, Exception) as error:
            messages.error(request, 'Error connecting to the database.')
            print(error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    return render(request, 'dlogin.html')







def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dlogin.html') 
    else:
        form = DoctorRegistrationForm()
    return render(request, 'dregistration.html', {'form': form})



def availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html') 
    else:
        form = AvailabilityForm()
    return render(request, 'availability.html', {'form': form})


def dhome(request):
    return render(request, 'dhome.html')


def display_field(request):

    field_data = Doctor.objects.values_list('', flat=True)

    context = {
        'field_data': field_data,
    }

    return render(request, '1.html', context)