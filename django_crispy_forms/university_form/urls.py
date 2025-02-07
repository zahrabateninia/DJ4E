from django.urls import path
from .views import   index # Import your view function

urlpatterns = [
    path('', index , name='index'),  # Homepage
]
