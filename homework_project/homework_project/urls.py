from django.conf import settings

from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('learning/', include('learning.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns