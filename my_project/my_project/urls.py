# """
# URL configuration for my_project project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from my_app.views import *
# from contact.views import *


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("home", home, name="home"),
#     path("contact", contact_us, name="contact"),
#     path("login/", include("user_login.urls")),
#     path("login/", include("django.contrib.auth.urls")),
# ]

from django.contrib import admin
from django.urls import path, include
from my_app.views import *
from contact.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home, name="home"),
    path("contact/", contact_us, name="contact"),
    path("user_login/", include("user_login.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    ]