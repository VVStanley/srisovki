from django.urls import path
from posts.views import Category, Post, post_like,\
    post_add_wishlist, post_remove_wishlist, SearchPosts


app_name = 'posts'

urlpatterns = [
    path('post_like/<int:pk>/', post_like, name='post_like'),
    path('post_add_wishlist/<int:pk>/', post_add_wishlist, name='post_add_wishlist'),
    path('post_remove_wishlist/<int:pk>/', post_remove_wishlist, name='post_remove_wishlist'),
    path('search/', SearchPosts.as_view(), name='search'),

    # Эти 2 роута всегда внизу! они все съедают
    path('<slug:slug>/', Category.as_view(), name="category"),
    path('srisovka/<slug:slug>/', Post.as_view(), name="post")
]
