from django import forms
from .models import Doctor
from .models import Availability

class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'age', 'experience', 'specialization', 'photo', 'mobile', 'email', 'address','username','password']



class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['Doctor','available_date', 'available_time']




class DoctorLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
