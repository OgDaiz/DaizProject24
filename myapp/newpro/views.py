from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup_view(request):

    return render(request, 'signup.html')

def login_view(request):

    return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile

def signup_view(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.userprofile.matric_number = form.cleaned_data.get('matric_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('dashboard_view')
    else:
        form = UserProfile()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    # Your login view logic here
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
