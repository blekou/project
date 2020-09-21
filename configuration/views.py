from django.shortcuts import render
from .models import About, Contact

def contact(request):
    
    data = {

    }
    return render(request, 'pages2/contact.html', data)


def about(request):
    abouts = About.objects.filter()[:1]

    data = {
        'abouts':abouts,
    }
    return render(request, 'pages2/about.html', data)