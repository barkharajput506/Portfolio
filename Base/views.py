from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, Http404
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import messages
from Base.models import Contact
from Base import models
from Base.forms import ContactForm
import os
from django.conf import settings


def home(request):
    return render(request, 'Base/home.html')

def about(request):
    return render(request, 'Base/about.html')

def projects(request):
    projects_show = [
        {
            'title': 'E-Commerce Website',
            'path':  'Base/images/ecomerceweb.png',
        },
        {
            'title': 'Library Management System',
            'path': 'Base/images/libimg.png',
        },
        {
            'title': 'Portfolio Website',
            'path': 'Base/images/portfolioimg.png',
        },
        {
            'title': 'Image Uploader',
            'path': 'Base/images/imageuploader.png',
        },
        {
            'title': 'Resume Uploader',
            'path': 'Base/images/resumeuploader.png',
        },   
        
    ]
    return render(request, 'Base/projects.html', {'projects_show':projects_show })


def experience(request):
    experience = [
        # {
        #     'company': 'ABC',
        #     'position': 'python developer',
        # },
        # {
        #     'company': 'ABC1',
        #     'position': 'python developer1',
        # },
        # {
        #     'company': 'ABC2',
        #     'position': 'python developer2',
        # },
    ]
    return render(request, 'Base/experience.html', {'experience':experience})
   


def certificate(request):
    certificate_show = [
        {
            'title': 'AWS',
            'path':  'Base/images/awscer.png',
        },
        {
            'title': 'Python',
            'path': 'Base/images/pythoncer.jpg',
        },    
    ]
    return render(request, 'Base/certificate.html', {'certificate_show':certificate_show })
    


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Submit successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'Base/contact.html', {'form': form})
    


def resume(request):
    RESUME_RELATIVE_PATH = 'Base/doc/resume.pdf'
    file_path = os.path.join(settings.STATIC_ROOT, RESUME_RELATIVE_PATH)
    if not os.path.exists(file_path):
        print(f"ERROR: Resume file not found at expected path: {file_path}")
        return HttpResponse("Resume file not found.", status=404)
    
    try:
        file_handle = open(file_path, 'rb')
        response = FileResponse(file_handle, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        return response
    except FileNotFoundError:
        return HttpResponse("Resume file not found.", status=404)
    except Exception as e:
        print(f"ERROR serving resume: {e}")
        return HttpResponse("An internal error occurred.", status=500)

    # resume_path = 'Base/doc/resume.pdf'
    # resume_path = staticfiles_storage.path(resume_path)
    # if staticfiles_storage.exists(resume_path):
    #     with open(resume_path, 'rb') as resume_file:
    #         response = HttpResponse(resume_file.read(), content_type="application/pdf")
    #         response['Content-Disposition']='attachment'; filename="resume.pdf"
    #         return response
        
    # else:
    #     return HttpResponse("resume not found", status=404)    
        



