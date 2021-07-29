from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap


sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("myadmin/", admin.site.urls),
    path("", include("blog.urls"), name="blog-urls"),
    path("",include("aboutblog.urls"),name='aboutblog-urls'),
    # path("summernote/", include("django_summernote.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('images/', include('ckeditor_uploader.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)