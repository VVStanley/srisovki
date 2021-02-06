from django.urls import path
from step_drawing.views import Home, CategoryOrPost, post_step_like


app_name = 'step_drawing'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post_step_like/<int:pk>/', post_step_like, name='post_step_like'),
    path('<slug:slug>/', CategoryOrPost.as_view(), name="category_or_post"),
    # path('post_add_wishlist/<int:pk>/', post_add_wishlist, name='post_add_wishlist'),
    # path('post_remove_wishlist/<int:pk>/', post_remove_wishlist, name='post_remove_wishlist'),
    # path('search/', SearchPosts.as_view(), name='search'),

    # # Эти 2 роута всегда внизу! они все съедают
    # path('<slug:slug>/', Category.as_view(), name="category"),
    # path('srisovka/<slug:slug>/', Post.as_view(), name="post")
]
