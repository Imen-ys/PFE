"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from rest_framework.urlpatterns import format_suffix_patterns
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/',views.send_message),
    path('http://127.0.0.1:7000',views.send_message),
    #path('message/', views.send_message, name='message'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)