from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginForm

# Create your views here.


def register(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', context={'registerForm': form})
