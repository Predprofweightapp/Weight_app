from django.shortcuts import render
from .forms import DataForm
from .models import UserData
from django.http import HttpRequest


def home(request):
    return render(request, "Register_page/home_page.html")


def reg(request):
    error = ''
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Register_page/transfers/transfer_to_auth.html")
        else:
            error = 'Please, enter a correct email!'

    form = DataForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, "Register_page/register_form.html", context)


def auth(request):
    error = ''
    # find_success = False
    users = UserData.objects.all()
    if request.method == 'POST':
        for i in users:
            if i.login == request.POST['login'] and i.password == request.POST['password']:
                # find_success = True
                return render(request, "Register_page/transfers/transfer_to_profile.html")
        else:
            error = 'Wrong login or password'
    form = DataForm()
    context = {
        'form': form,
        'error': error,
        'users': users
    }
    return render(request, "Register_page/auth_form.html", context)


def profile(request):
    return render(request, "Register_page/profile.html")
