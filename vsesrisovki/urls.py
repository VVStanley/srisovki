from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static


urlpatterns = [
    path('manatee/', admin.site.urls),
    path('apiws/v1/', include('api.urls')),

    path('accounts/', include('allauth.urls'), name='accounts'),
    path('accounts/profile/', include('users.urls'), name='profile'),

    path('obuchenie/', include('step_drawing.urls'), name='step_drawing'),

    # Эти 2 роута всегда внизу! posts последний!
    path('', include('front.urls')),
    path('', include('posts.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)