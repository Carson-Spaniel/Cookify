from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('library/',views.library, name='library'),
    path('login/',views.login, name='login'),
    path('home/',views.home, name='home'),
    path('process_string/', views.process_string, name='process_string'),
]
