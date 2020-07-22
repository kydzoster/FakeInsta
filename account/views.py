from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        # initiates the login form
        form = LoginForm(request.POST)
        # checks if form is valid, if it's not, displays an error
        if form.is_valid():
            cd = form.cleaned_data
            # checks user credentials and returns user object if they are correct
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                # if user was successfully authenticated, checks if it is active
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

# this will check if current user is authenticated, if he is not it will redirect user to login URL
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})