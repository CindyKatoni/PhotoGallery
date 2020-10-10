from django.shortcuts import render
from photos.models import Photos

# Create your views here.
def photo_index(request):
    photos = Photos.objects.all()
    context = {
        'photos':photos
    }
    return render(request, 'photo_index.html', context)

def photo_details(request, pk):
    photos = Photos.objects.get(pk=pk)
    context = {
        'photos':photos
    }  
    return render(request, 'photo_details.html', context)