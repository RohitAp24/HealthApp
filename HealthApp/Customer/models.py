from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100) 
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])

    def __str__(self):
        return self.username
    


class Appointment(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Doctor = models.ForeignKey('self', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')], max_length=20)

    class Meta:
        unique_together = ['Doctor', 'appointment_date', 'appointment_time']