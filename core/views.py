from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

def about(request):
    context = {
        "owner_name": "Tu Nombre",
        "owner_role": "Desarrollador",
        "owner_bio": "Breve descripción sobre vos. Intereses, experiencia y objetivo del blog.",
    }
    return render(request, "about.html", context)
