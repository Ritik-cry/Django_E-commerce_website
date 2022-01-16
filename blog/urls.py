from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome),
    path('blogPost/<int:id>', views.blogPost)
]