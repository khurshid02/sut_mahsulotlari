from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('register', views.registerPage),
    path('product/<str:pk>', views.product),
    path('category/<str:pk>', views.exact_category),
    path('search', views.search),
    path('search/<str:pk>', views.exact_search),
    path('contact', views.contact),
    path('cart/<str:pk>', views.cart_add),
    path('cart', views.cart_menu),
    path('delete/<int:pk>', views.delete),
    path('shop', views.shop),
    path('buy', views.buy),
    path('history', views.history),


]
