from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('signup/',views.register,name='signup'),
    path('display/',views.display,name='display'),
    path('bio/',views.bio,name='bio'),
]