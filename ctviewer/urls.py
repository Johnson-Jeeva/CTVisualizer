from django.urls import path
from .views import photo_upload, upload_success, home  

urlpatterns = [
    path('upload/', photo_upload, name='photo_upload'),
    path('success/', upload_success, name='photo_upload_success'),
    path('', home, name='home'), 
]