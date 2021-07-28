from . import views
from django.urls import include
import re
from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed

urlpatterns = [
    path('search/',views.post_search, name='post_search'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("aboutus", views.aboutus, name="aboutus"),
    path('tags/<slug:tag_slug>/',views.TagIndexView.as_view(), name='posts_by_tag'),
    path('category/<slug:slug>/', views.category,name='category'),
    
    
    

]

