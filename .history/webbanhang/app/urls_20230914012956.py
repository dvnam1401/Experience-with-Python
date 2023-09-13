from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.update_item, name='update_item'),
    path('cart/update_item/', views.update_item, name='update_item'),
]
