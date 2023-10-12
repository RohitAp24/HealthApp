from django.urls import path

from . import views
from .views import register_doctor
from .views import availability

urlpatterns = [path("dlogin", views.dlogin, name = 'dlogin.html'),
               path('dregister', register_doctor, name='register_doctor'),
               path('availability', views.availability, name='availability.html' ),
               path('dhome', views.dhome, name='dhome.html')
               
               ]
