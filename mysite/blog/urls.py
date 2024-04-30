from django.urls import path, re_path
from django.template.defaulttags import url
from . import views
from .feeds import LatestPostsFeed


urlpatterns = [
    # post views
    path('', views.post_list, name='base'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'), # r'(?P<post>[-\w]+)/$'
    path('', views.post_list, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
