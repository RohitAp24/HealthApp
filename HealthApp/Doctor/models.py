from django.db import models
from django.contrib.auth.hashers import check_password
import logging


# Create your models here.

logger = logging.getLogger(__name__)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    experience = models.IntegerField()
    specialization = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors/')
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()

    class Meta:
        db_table = 'doctor_table'

    def check_password(self, raw_password):
        logger.debug(f"Entered password: {raw_password}")
        logger.debug(f"Doctor password hash: {self.password}")
        result = check_password(raw_password, self.password)
        logger.debug(f"Password comparison result: {result}")
        return result




class Availability(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    available_date = models.DateField()
    available_time = models.TimeField()

    class Meta:
        unique_together = ['Doctor', 'available_date', 'available_time']