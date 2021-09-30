from django.urls import path
from .views import (
    BlogCreateView,
    BlogListView, 
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('posts/new/', BlogCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/update/', BlogUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    
]