from django.urls import path


from . import views

urlpatterns = [path("", views.index, name ="index1234.html"),
               path("login/", views.user_login, name ="login.html"),
               path("registration", views.register_user, name ="reg.html"),
               path("appointment", views.appointment, name ="appointment.html"),
               path("chome", views.chome, name='chome.html')
               ]