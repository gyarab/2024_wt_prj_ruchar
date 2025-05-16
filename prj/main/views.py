from django.shortcuts import render

from .models import Painting, ArtMovement

# Create your views here.

def get_homepage(request):
    paintings = Painting.objects.all().order_by('name')
    
    search = request.GET.get('search')
    if search:
        paintings = paintings.filter(name__icontains=search) | paintings.filter(description__icontains=search)

    art_movement = request.GET.get('artmovement')
    if art_movement:
        paintings = paintings.filter(art_movement__name=art_movement)

    context = {
        "paintings": paintings,
        "art_movements": ArtMovement.objects.all().order_by('name'),
    }

    return render(
        request, "main/homepage.html", context
        )

def get_painting(request, pk):
    painting = Painting.objects.get(pk=pk)
    context = {
        "painting": painting,
    }
    return render(request, "main/detail.html", context)