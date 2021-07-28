from .models import Category


def category_renderer(request):
    return {
       'all_category': Category.objects.all()
    }