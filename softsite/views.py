from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout

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
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "softsite/login.html",context)