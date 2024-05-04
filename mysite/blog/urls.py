from django.urls import path, re_path
from . import views
from .feeds import LatestPostsFeed
from .views import (
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # post views
    path('', views.post_list, name='base'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    # post CRUD ops
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    # about func url
    path('about/', views.about, name='blog-about'),
]
