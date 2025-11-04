from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Page(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=250)
	content = RichTextField()
	image = models.ImageField(upload_to='pages/', blank=True, null=True)
	pub_date = models.DateField(auto_now_add=True)
	slug = models.SlugField(unique=True, max_length=220, blank=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	class Meta:
		ordering = ['-pub_date']
		verbose_name = 'Página'
		verbose_name_plural = 'Páginas'

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)[:220]
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title
