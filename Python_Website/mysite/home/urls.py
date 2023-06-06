from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('process_string/', views.process_string, name='process_string'),
]
