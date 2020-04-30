from . models import *
from django import forms
from django.contrib.auth.forms import *
from .models import Student

User = get_user_model()

class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This User is not active')

        log = super(UserLogin, self).clean(*args, **kwargs)
        return log


class StudentForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop('request',None)
        super(StudentForm,self).__init__(*args,**kwargs)

    class Meta:
        model = Student
        fields = [
            'rollNo','firstName','lastName'
        ]