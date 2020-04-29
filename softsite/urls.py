from django.urls import path
from . import views

app_name = 'softsite'
urlpatterns = [
    path('login/',views.userLogin, name='login'),
    ]