"""django2 URL Configuration

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
from gtapp import views
from gtapp.views import CallView
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.mainFunc), # 요청명이 없을때는 view.mainFunc로 간다. 1. Function views 
    path('abc/callget', CallView.as_view()),    # 2. Class-based views
    path('member/', include('gtapp.urls'))  # 3. Including another URLconf 위임
]
