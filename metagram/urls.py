from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('display/',views.display,name='display'),
    path('bio/',views.bio,name='bio'),
]