from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# Create your models here.

class Aboutblog(models.Model):
    image = models.ImageField(upload_to='media')
    about = RichTextUploadingField(config_name='custom',blank=True, null=True)
    disclaimer = RichTextUploadingField(config_name='custom',blank=True, null=True)
    policy = RichTextUploadingField(config_name='custom',blank=True, null=True)
    twitter = models.CharField(max_length=255)
    linkdin = models.CharField(max_length=255)
    github = models.CharField(max_length=255)



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    blogrequest = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Footer(models.Model):
    about = models.TextField()
    categories = models.CharField(max_length=255)
    pages = models.CharField(max_length=255)
    Connect = models.CharField(max_length=255)
