from django.urls import path
from . import views

app_name = 'softsite'
urlpatterns = [
    path('login/',views.userLogin, name='login'),
    path('addStudent/',views.StudentView, name='addStudent'),
    path('success/',views.SuccessView.as_view(), name='success'),
]