from django.shortcuts import render, HttpResponse
from home import models
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def skills(request):
    return render(request, 'skills.html')


def projects(request):
    return render(request, 'projects.html')


def statistics(request):
    return render(request, 'statistics.html')


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        print("data written to db")

    return render(request, 'contact.html')
