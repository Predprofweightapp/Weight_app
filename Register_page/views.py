from django.shortcuts import render, redirect
from .forms import DataForm
from .models import UserData


def reg(request):
    error = ''
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('collect')
        else:
            error = 'Please, enter a correct email!'

    form = DataForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "Register_page/register_form.html", context)


def auth(request):
    error = ''

    users = UserData.objects.all()
    if request.method == 'POST':
        form = DataForm(request.POST)
        for i in users:
            if i.login == form.login:

    form = DataForm()
    context = {
        'form': form,
        'error': error,
        'users':users
    }
    return render(request, "Register_page/auth_form.html", context)
