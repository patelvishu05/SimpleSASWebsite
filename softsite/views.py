from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView
from . forms import *


# Create your views here.
def userLogin(request):
    next = request.GET.get('next')
    form = UserLogin(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('softsite:addStudent')

    context = {
        'form': form,
    }
    return render(request, "softsite/login.html",context)


def StudentView(request):
    form = StudentForm(request=request.POST or None)
    if form.is_valid():
        form.save(using=request.user)
        return redirect('softsite:success')
    else:
        print(form.errors)
    context = {
        'form' : form,
        'user' : request.user,
    }
    return render(request,"softsite/addStudent.html",context)


class SuccessView(TemplateView):
    template_name = "softsite/success.html"

    def get(self, request):
        currentUser = request.user

        args = {'currentUser':currentUser}
        return render(request,self.template_name,args)

    def post(self,request):
        currentUser = request.user
        print(request.POST)
        args = {'currentUser': currentUser}
        return render(request, self.template_name, args)