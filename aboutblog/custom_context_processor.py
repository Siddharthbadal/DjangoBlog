from .models import Footer


def footer_renderer(request):
    return {
       'footer': Footer.objects.all()
    }