from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    # path('about/', views.about, name="Aboutus"),
    path('contact/', views.contact, name="ContactUs"),
    # path('productview/', views.productview, name="Product View"),
    path('tracker/', views.tracker, name="Tracking"),
    # path('checkout/', views.checkout, name="Checkout"),
    # path('shop/', views.shop, name="Shop"),
    path('shopCategory/', views.shopCategory, name="Shop Category"),
    path('prodctDetails/', views.prodctDetails, name="Prodct Details"),
    path('prodctCheckout/', views.prodctCheckout, name="prodct Checkout"),
    path('shopingCart/', views.shopingCart, name="shoping Cart"),
    path('confirmation/', views.confirmation, name="Confirmation"),
    path('contact/', views.contact, name="Contact"),
    path('profile/', views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop/logout.html'), name="logout"),
    path('registration/', views.register, name="register")
]