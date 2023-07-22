from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def view_contacts(request):
    return render(request, 'contactme/contactme.html')

def view_education(request):
    return render(request, 'education/education.html')

def view_aboutme(request):
    return render(request, 'aboutmeview/aboutmeview.html')

def view_resume(request):
    return render(request, 'resume/resume.html')