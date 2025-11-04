from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
from .forms import PageForm

class PageListView(ListView):
	model = Page
	template_name = 'pages/page_list.html'
	context_object_name = 'pages'

class PageDetailView(DetailView):
	model = Page
	template_name = 'pages/page_detail.html'
	context_object_name = 'page'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'

class PageCreateView(LoginRequiredMixin, CreateView):
	model = Page
	form_class = PageForm
	template_name = 'pages/page_form.html'
	success_url = reverse_lazy('pages:list')

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.author = self.request.user
		obj.save()
		return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
	model = Page
	form_class = PageForm
	template_name = 'pages/page_form.html'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'
	success_url = reverse_lazy('pages:list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
	model = Page
	template_name = 'pages/page_confirm_delete.html'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'
	success_url = reverse_lazy('pages:list')
