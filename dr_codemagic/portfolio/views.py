
from django.shortcuts import render
from .models import Profile, Service,Project

def portfolio_view(request):
    profile = Profile.objects.first()
    services = Service.objects.filter(is_active=True)
    context = {
        'profile': profile,
        'services': services,
    }
    return render(request, 'index.html', context)

def about_view(request):
    profile = Profile.objects.first()
    services = Service.objects.filter(is_active=True)
    context = {
        'profile': profile,
        'services': services,
    }
    return render(request, 'about.html', context)

def contact_view(request):
    return render(request, 'contact.html')

def projects(request):
    projects = Project.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'projects.html', {  # نام قالب هم تغییر کرد
        'projects': projects
    })

