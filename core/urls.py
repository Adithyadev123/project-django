from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = []

# ✅ STATIC FIRST (CRITICAL)
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

# ✅ THEN normal routes
urlpatterns += [
    path('admin/', admin.site.urls),
    path('', include('admin_black.urls')),
    path('', include('home.urls')),
]


