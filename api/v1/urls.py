from rest_framework.urls import path
from . import views

urlpatterns = [
    path('generate_presentation/', views.GeneratePresentation.as_view(), name='generate_presentation'),
]