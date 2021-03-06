"""hackathon2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls as auth_urls

from hackathon2018 import settings
from students import views

urlpatterns = [
    path('admin_dashboard/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include(auth_urls)),
    path('accounts/profile/', views.index, name='index'),
    path('students/', include('students.urls')),
    # path('test/', include(auth_urls)),
    path('logout/', views.user_logout, name='logout'),
    path('portal/', views.portal, name='portal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)