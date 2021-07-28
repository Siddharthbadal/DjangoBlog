from . import views
from django.urls import path

urlpatterns = [
    path('policy',views.policy, name='policy'),
    path('disclaimer', views.disclaimers, name='disclaimer'),
    path('contact', views.contact, name='contact')
]