from django.shortcuts import render

from .models import Painting

# Create your views here.

def get_homepage(request):
    paintings = Painting.objects.all().order_by('name')
    
    if request.GET.get("search"):
        print("SEARCH", request.GET.get("search"))
        paintings = paintings.filter(name__contains=request.GET.get("search"))

    context = {
        "svatek": "Marek",
        "paintings": paintings
    }

    # print("HOST", request.get_host())
    # print("URL", request.path)

    return render(
        request, "main/homepage.html", context
        )