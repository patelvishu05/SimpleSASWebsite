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
    form = StudentForm(request=request)
    if request.method == 'POST':
        form = StudentForm(request.POST, request=request)
        print("---->")
        print(form.errors)
        print(form.is_valid())
        print(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save(using=str(request.user))
            audit = AuditTrail(rollNo=instance, comments="Added " + instance.firstName)
            audit.save()
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