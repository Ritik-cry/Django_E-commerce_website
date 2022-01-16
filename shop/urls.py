from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopHome),
    path('about/', views.about),
    path('tracker/', views.tracker),
    path('contact/', views.contact),
    path('product/<int:myid>', views.product),
    path('cart/', views.cart),
    path('search/', views.search)
]