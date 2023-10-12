import logging
from django.contrib.auth.backends import BaseBackend
from .models import Doctor

logger = logging.getLogger(__name__)

class CustomDoctorBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        logger.info(f"Authenticating user: {username}")
        try:
            doctor = Doctor.objects.using('default').only('email', 'password').get(email=username)
            logger.info(f"Retrieved doctor: {doctor}")
            logger.info(f"Entered password: {password}")
            logger.info(f"Doctor password: {doctor.password}")
            if doctor.check_password(password):
                logger.info("Password is correct")
                return doctor
            else:
                logger.info("Password is incorrect")
        except Doctor.DoesNotExist:
            logger.info("Doctor does not exist")
            return None

    def get_user(self, user_id):
        try:
            return Doctor.objects.using('default').get(email=user_id)
        except Doctor.DoesNotExist:
            return None
