"""
URL configuration for appleBizCraftDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views as my_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_views.home_one, name='home-one-url'),
    path('home-two/', my_views.home_two, name='home-two-url'),
    path('home-three/', my_views.home_three, name='home-three-url'),
    path('home-four/', my_views.home_four, name='home-four-url'),
    path('about-one/', my_views.about_one, name='about-one-url'),
    path('about-two/', my_views.about_two, name='about-two-url')
]
