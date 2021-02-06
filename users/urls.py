from django.urls import path
from users.views import Detail, Settings, Wishlist, UserAddPost

app_name = 'profile'


urlpatterns = [

    path('', Detail.as_view(), name='detail'),
    path('settings/', Settings.as_view(), name='settings'),
    path('wishlist/', Wishlist.as_view(), name='wishlist'),
    path('add_post/', UserAddPost.as_view(), name='add_post'),
]
