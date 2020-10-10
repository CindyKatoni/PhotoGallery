from django.shortcuts import render
from photos.models import Photos

# Create your views here.
def photo_index(request):
    photos = Photos.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'photo_index.html', context)