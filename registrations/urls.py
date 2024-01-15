from django.urls import path
from .views import UserRegistrationView

app_name = 'registrations'

urlpatterns = [
    path('signup', UserRegistrationView.as_view(),name="login")
]