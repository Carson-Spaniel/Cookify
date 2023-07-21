from django.urls import path
from . import views

urlpatterns = [
    #----------------Pages----------------
    path('',views.recipesPage, name='recipes-page'),
    # path('index/',views.index, name='index'),
    path('recipes-page/',views.recipesPage, name='recipes-page'),
    path('breakfast/',views.breakfast, name='breakfast'),
    path('lunch/',views.lunch, name='lunch'),
    path('dinner/',views.dinner, name='dinner'),
    path('beef/',views.beef, name='beef'),
    path('chicken/',views.chicken, name='chicken'),
    path('italianSausage/',views.italianSausage, name='italianSausage'),
    # path('snacks/',views.snacks, name='snacks'),
    path('dessert/',views.dessert, name='dessert'),

    #----------------requests----------------
    path('searchRecipe/', views.searchRecipe, name='searchRecipe'),
    # path('login_info/', views.login_info, name='login_info'),

    # ------------- breakfast pages -------------
    path('breakfastCasserole/',views.breakfastCasserole, name='breakfastCasserole'),

    # ------------- lunch pages -------------
    path('macAndCheese/',views.macAndCheese, name='macAndCheese'),

    # ------------- beef pages -------------
    path('tacoSoup/',views.tacoSoup, name='tacoSoup'),

    # ------------- chicken pages -------------
    path('tuscChick/',views.tuscChick, name='tuscChick'),
    path('chickTortel/',views.chickTortel, name='chickTortel'),
    path('kRC/',views.kRC, name='kRC'),
    path('teriakiChick/',views.teriakiChick, name='teriakiChick'),
    path('hGC/',views.hGC, name='hGC'),

    # ------------- italian sausage pages -------------
    path('mendicino/',views.mendicino, name='mendicino'),

    # ------------- snack pages -------------


    # ------------- dessert pages -------------
    path('kSC/',views.kSC, name='kSC'),
    path('rCB/',views.rCB, name='rCB'),

]
