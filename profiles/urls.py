from django.urls import path
from .views import profile_detail, profile_update, ProfilePasswordChangeView

app_name = 'profiles'

urlpatterns = [
	path('', profile_detail, name='detail'),
	path('edit/', profile_update, name='edit'),
	path('password/', ProfilePasswordChangeView.as_view(), name='password'),
]
