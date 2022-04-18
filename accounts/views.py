from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import LogInForm, SignUpForm


def login(request):
    if request.method == 'POST':
        form = LogInForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(request.GET.get('next', '/'))

        return render(request, 'accounts/login.html', {'form': form})

    form = LogInForm()
    return render(request, 'accounts/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, 'accounts/signup.html', {'form': form})

    form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
