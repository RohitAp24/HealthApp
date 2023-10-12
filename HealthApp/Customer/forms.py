from django import forms
from .models import Customer
from .models import Appointment


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'name', 'age', 'email', 'phone','username', 'password', 'gender']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['Doctor', 'appointment_date','appointment_time']


class CustomerLoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

