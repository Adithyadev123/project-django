from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('', include('admin_black.urls')),
    path('admin/', admin.site.urls),
]

# ✅ THIS IS REQUIRED TO SERVE STATIC FILES (DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

