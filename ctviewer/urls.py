from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.photo_upload, name='photo_upload'),
    path('success/', views.upload_success, name='photo_upload_success'),
]