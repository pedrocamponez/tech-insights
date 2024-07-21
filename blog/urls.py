from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.api.viewsets import PostViewSet, CommentViewSet
from blog.views import PostListView, PostCreateView, post_edit, post_delete
from django.contrib.auth.views import LogoutView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
]
