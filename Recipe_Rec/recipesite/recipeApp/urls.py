from django.urls import path
from . import views

urlpatterns = [
    #----------------Pages----------------
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('recipes/',views.recipes, name='recipes'),

    #----------------requests----------------
    path('process_string/', views.process_string, name='process_string'),
    # path('login_info/', views.login_info, name='login_info'),
]
