from django.urls import path
from . import views
app_name = 'todooapp'



urlpatterns = [

    path('', views.home, name='home'),


]
