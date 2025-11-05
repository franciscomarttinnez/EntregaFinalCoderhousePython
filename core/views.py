from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

def about(request):
    context = {
        "owner_name": "Francisco Martinez",
        "owner_role": "Desarrollador",
        "owner_bio": "Desarrollando pagina de blog entrega final coderhouse",
    }
    return render(request, "about.html", context)
