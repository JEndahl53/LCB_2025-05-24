# core/urls.py
"""
URL configuration for the core project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from common.views import HomePageView
from django.conf.urls.static import static
from django.conf import settings


# Import the view we created in core/views.py


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # Django Admin
    path("admin/", admin.site.urls),
    # User Management
    path("accounts/", include("django.contrib.auth.urls")),
    # Local Apps
    path("concerts/", include("concerts.urls")),
    path("library/", include("library.urls")),
    path("favicon.png", RedirectView.as_view(url="/static/favicon.png")),
]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
