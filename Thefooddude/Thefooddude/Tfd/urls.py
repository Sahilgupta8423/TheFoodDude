from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name ="Home"),
    path("cart/", views.cart, name ="Cart"),
    path("help/", views.help, name ="Help"),
    path("profile/", views.profile, name ="Help"),
    path("search/", views.search, name ="Help"),
    path("<int:myid>/", views.resView, name ="restaurants"), 
    
] 