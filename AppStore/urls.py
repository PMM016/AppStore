from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),

    path("nav/", load_nav, name="load_nav"),

    # Apps app
    path("apps/", include("apps.urls", namespace="apps")),

    # Accounts app (assuming you’ll add)
    path("accounts/", include("accounts.urls", namespace="accounts")),

    # # APIs app placeholder
    # path("apis/", include("apis.urls", namespace="apis")),

    # # Passwords app placeholder
    # path("pass/", include("passwords.urls", namespace="passwords")),

    # # Sites app placeholder
    # path("sites/", include("sites.urls", namespace="sites")),

    # # Home / root page
    # path("", include("home.urls", namespace="home")),

    path("back/", go_back, name="back"),

]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
