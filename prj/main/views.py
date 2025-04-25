from django.shortcuts import render

from .models import Painting

# Create your views here.

def get_homepage(request):
    context = {
        "svatek": "Marek",
        "paintings": Painting.objects.all().order_by('name') [:10]
    }
    return render(
        request, "main/homepage.html", context
        )