from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import SignUpForm

class UserLoginView(LoginView):
	template_name = "accounts/login.html"

class UserLogoutView(LogoutView):
	next_page = reverse_lazy('home')

def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso. Sesión iniciada.")
			return redirect('pages:list')
		else:
			messages.error(request, "Revisá los errores del formulario.")
	else:
		form = SignUpForm()
	return render(request, "accounts/signup.html", {"form": form})
