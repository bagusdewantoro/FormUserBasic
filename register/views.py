from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    userlist = User.objects.exclude(username='admin')
    return render(request, 'register/home.html', {'user': userlist})

def register(request):
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            print(userform)
            print(userform.cleaned_data)
            userform.save()
            return redirect('home')
    else:
        userform = UserCreationForm()
    return render(request, 'register/register.html', {'form': userform})
