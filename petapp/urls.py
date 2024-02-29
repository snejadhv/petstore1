from django.urls import path
from .views import PetDetailView

urlpatterns = [
    path('<int:pk>/', PetDetailView.as_view(), name='detail'),
]