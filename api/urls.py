from rest_framework import routers

from api.posts.views import CategoryApiView
from api.front.views import WhatColorizeApiView
from api.comments.views import CommentsView

app_name = 'api'


router = routers.DefaultRouter()

router.register(r'what_colorize', WhatColorizeApiView, 'what_colorize')
router.register(r'category', CategoryApiView, 'category')
router.register(r'comments', CommentsView, 'comments')

urlpatterns = router.urls
