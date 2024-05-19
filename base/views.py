from django.shortcuts import render
from base.models import Contact
from datetime import datetime
def index(request):
    return render(request, "index.html")
    
def achivements(request):
    return render(request, "achivements.html") 

def about(request):
    return render(request , "about.html")

def contact(request):
    if request.method == 'POST':
        fristname = request.POST.get('fristname') 
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        massage = request.POST.get('massage') 
        contact = Contact(fristname = fristname , lastname = lastname , email = email , massage = massage)
        contact.save()
    return render(request , "contact.html")        

def projects(request):
    return render(request , "projects.html")