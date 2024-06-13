"""
URL configuration for gaflix project.

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
from django.views.generic import TemplateView

from filmy.views import movies, movie, director, directors, actor, actors

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="filmy/prvni.html")),
    path("druha/", TemplateView.as_view(template_name="filmy/druha.html")),
    path("filmy/", movies, name="movies"),
    path("film/<int:id>", movie, name="movie"),
    path("herci/", actors, name="actors"),
    path("herec/<int:id>", actor, name="actor"),
    path("reziseri/", directors, name="directors"),
    path("reziser/<int:id>", director, name="director"),
]

