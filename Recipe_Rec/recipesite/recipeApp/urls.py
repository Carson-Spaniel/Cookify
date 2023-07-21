from django.urls import path
from . import views

urlpatterns = [
    #----------------Pages----------------
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('recipesPage/',views.recipesPage, name='recipesPage'),
    path('breakfast/',views.breakfast, name='breakfast'),
    path('lunch/',views.lunch, name='lunch'),
    path('dinner/',views.dinner, name='dinner'),
    path('snacks/',views.snacks, name='snacks'),
    path('dessert/',views.dessert, name='dessert'),

    #----------------requests----------------
    path('searchRecipe/', views.searchRecipe, name='searchRecipe'),
    # path('login_info/', views.login_info, name='login_info'),
]
