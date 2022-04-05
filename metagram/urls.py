from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('signup/',views.register,name='signup'),
    path('display/',views.display,name='display'),
    path('bio/',views.bio,name='bio'),
]