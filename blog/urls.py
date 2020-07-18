from django.contrib import admin
from django.urls import path,include
from .views import PostListView,post_detail,PostCreateView,PostUpdateView,UserPostListView,PostDeleteView,EditComment,DeleteComment
from . import views

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('post/<int:id>/', post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pid>/edit-comment/<int:cid>/', EditComment, name='edit-comment'),
    path('post/<int:pid>/delete-comment/<int:cid>/', DeleteComment, name='delete-comment'),
]


