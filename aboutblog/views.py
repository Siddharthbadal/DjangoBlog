from django.shortcuts import render
from .models import Aboutblog, Contact, Footer



def footerview(request):
    footer = Footer.objects.all()
    context = {
        'footer':footer
    }
    return render(request, 'footer.html', context)
    
def policy(request):
    aboutblog = Aboutblog.objects.all()
    context = {
        'aboutblog':aboutblog
    }
    return render(request, 'policy.html', context)

def disclaimers(request):
    disclaimer = Aboutblog.objects.all()
    context = {
        'disclaimer': disclaimer
    }
    return render(request, 'disclaimer.html', context)

def contact(request):
    contact = Contact.objects.all()
    context = {
        'contact':contact
    }
    return render(request, 'contact.html', context)
