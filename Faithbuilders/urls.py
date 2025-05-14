"""
URL configuration for Faithbuilders project.

The `urlpatterns` list routes URLs to views. For more information please see:
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.api.urls')), 
    path('api/accounts/', include('accounts.api.urls')),
    path('api/cms/', include('cms.api.urls')), # this is where your API lives
    path('api/bot/', include('bot.api.urls')),
    path('', include('blog.urls')),
    path('cms/', include('cms.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('bot/', include('bot.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
