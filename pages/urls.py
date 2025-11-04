from django.urls import path
from .views import (
	PageListView, PageDetailView,
	PageCreateView, PageUpdateView, PageDeleteView
)

app_name = 'pages'

urlpatterns = [
	path('', PageListView.as_view(), name='list'),
	path('create/', PageCreateView.as_view(), name='create'),
	path('<slug:slug>/', PageDetailView.as_view(), name='detail'),
	path('<slug:slug>/edit/', PageUpdateView.as_view(), name='edit'),
	path('<slug:slug>/delete/', PageDeleteView.as_view(), name='delete'),
]
