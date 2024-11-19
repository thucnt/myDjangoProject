from django.contrib.messages.context_processors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def app_homepage(request):
    return  render(request, 'homepage.html')

def about_us(request):
    return render(request, 'aboutUs.html')

def services(request):
    return render(request, 'services.html')

def contact_us(request):
    return render(request, 'contactUs.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("signin")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)