from django.contrib import admin
from django.urls import path, include
from blogs import views

urlpatterns = [
    path('', include('accounts.urls.v2')),
    path('', include('blogs.urls.v2')),

]
