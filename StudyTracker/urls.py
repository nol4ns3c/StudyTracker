from django.urls import path

from . import views

urlpatterns = [
    path('checkanswers/', views.checkanswers),
]
