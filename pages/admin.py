from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'subtitle', 'pub_date', 'author')
	search_fields = ('title', 'subtitle', 'content')
	list_filter = ('pub_date', 'author')
	prepopulated_fields = {"slug": ("title",)}
