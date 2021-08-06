from django.shortcuts import render, HttpResponse
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
    if request.method=="POST":
        contact = Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.name = name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return render(request, 'contact.html')       
    return render(request, 'contact.html')
