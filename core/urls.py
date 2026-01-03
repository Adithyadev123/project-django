from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_black.urls')),
    path('', include('home.urls')),
]

# ✅ CORRECT way to serve static files in DEBUG mode
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()


