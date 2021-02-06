from django.urls import path

from front.views import Home, FeedBack, TermsOfUse,\
    RightHolders, Sitemap, CookieRules, WhatRegister, WhatColorize


app_name = 'front'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('terms-of-use/', TermsOfUse.as_view(), name='terms_of_use'),
    path('feedback/', FeedBack.as_view(), name='feedback'),
    path('what-register/', WhatRegister.as_view(), name='what_register'),
    path('right-holders/', RightHolders.as_view(), name='right_holders'),
    path('cookie_rules/', CookieRules.as_view(), name='cookie_rules'),
    path('sitemap/', Sitemap.as_view(), name='sitemap'),
    path('what_colorize/', WhatColorize.as_view(), name='what_colorize'),
]
