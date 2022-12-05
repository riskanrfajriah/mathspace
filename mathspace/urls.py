"""mathspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from about.views import about
from courses.views import courses
from home.views import home
from guru.views import loginguru
from siswa.views import loginsiswa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('courses/', courses),
    path('home/', home),
    path('loginguru/', loginguru),
    path('loginsiswa/', loginsiswa),
]
