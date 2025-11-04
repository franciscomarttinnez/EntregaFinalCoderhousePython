from django.urls import path
from .views import inbox, sent, detail, compose

app_name = 'messenger'

urlpatterns = [
	path('', inbox, name='inbox'),
	path('sent/', sent, name='sent'),
	path('new/', compose, name='compose'),
	path('<int:pk>/', detail, name='detail'),
]
