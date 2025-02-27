from django.shortcuts import render, redirect
from .forms import PhotoForm
from django.http import HttpResponse


def photo_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_upload_success')
    else:
        form = PhotoForm()
    return render(request, 'photos/upload_photo.html', {'form': form})

def upload_success(request):
    return render(request, 'photos/upload_success.html')


def home(request):
    return HttpResponse("Welcome to the Photo Upload Site!")
