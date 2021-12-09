from django.urls import path
from . import views

urlpatterns = [
    path('', views.title),
    path('views/', views.description),
    path('views/', views.comments)
]
