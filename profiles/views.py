from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserUpdateForm, ProfileUpdateForm, MyPasswordChangeForm

@login_required
def profile_detail(request):
	# View con decorador, cumple el requisito
	return render(request, 'profiles/profile_detail.html')

@login_required
def profile_update(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, 'Perfil actualizado correctamente.')
			return redirect('profiles:detail')
		else:
			messages.error(request, 'Revisá los errores del formulario.')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	return render(request, 'profiles/profile_form.html', {'u_form': u_form, 'p_form': p_form})

class ProfilePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
	form_class = MyPasswordChangeForm
	template_name = 'profiles/password_change.html'
	success_url = reverse_lazy('profiles:detail')

	def form_valid(self, form):
		messages.success(self.request, 'Contraseña cambiada correctamente.')
		return super().form_valid(form)
