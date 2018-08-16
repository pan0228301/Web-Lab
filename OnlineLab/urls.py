"""OnlineLab URL Configuration

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
from django.contrib import admin
from django.urls import path,re_path
from main import views as main_view
from user import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', main_view.index ,name='index-url'),
    re_path(r'^content/(\d+)$', main_view.content, name='content-url'),
    re_path(r'^run/(\d+)$', main_view.run, name='run-url'),
    re_path(r'^logout/$', main_view.logout, name='logout'),
]
