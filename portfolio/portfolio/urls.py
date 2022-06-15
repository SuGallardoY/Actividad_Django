"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from portfolio.views import inicio, contacto, galeria, login, tienda, recover_login, register, tracking, donacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', inicio),
    path('contacto/', contacto),
    path('galeria/', galeria),
    path('login/', login),
    path('tienda/', tienda),
    path('recover/', recover_login),
    path('register/', register),
    path('tracking/', tracking),
    path('donacion/', donacion),
]
