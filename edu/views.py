from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course, Lesson
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def index(request):
    return HttpResponse("Welcome")

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/sign-up.html', {'form': form})

    
    
def sign_in(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['username'] = post_data.get('phone_number')  # Copy phone_number to username
        form = CustomUserLoginForm(request, data=post_data)
        print (form.is_valid())
        if form.is_valid():
            phone_number = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, phone_number=phone_number, password=password)
    
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                form.add_error(None, 'Invalid login or password')
        else:
            print("Form errors:", form.errors)
    else:
        form = CustomUserLoginForm()

    return render(request, 'registration/sign-in.html', {'form': form})
