from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import StudentCourses
from .forms import StudentCoursesForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    form = StudentCoursesForm

    if request.method == 'POST':
        form = StudentCoursesForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()


    context = {"form": form}
    return render(request, 'Courses/index.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'Courses/login.html', context)

def loginPage(request):
    if request.method == 'POST':
       username =  request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request, username=username, password=password)

       if user is not None:
            login(request, user)
            return redirect('index')
    context = {}
    return render(request, 'Courses/login.html', context)
