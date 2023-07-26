from django.urls import path
from . import views

urlpatterns = [
    #----------------Pages----------------
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('indexPage/',views.indexPage, name='indexPage'),
    path('recipes-page/',views.recipesPage, name='recipes-page'),
    path('breakfast/',views.breakfast, name='breakfast'),
    path('lunch/',views.lunch, name='lunch'),
    path('dinner/',views.dinner, name='dinner'),
    path('beef/',views.beef, name='beef'),
    path('chicken/',views.chicken, name='chicken'),
    path('italian-sausage/',views.italianSausage, name='italianSausage'),
    # path('snacks/',views.snacks, name='snacks'),
    path('dessert/',views.dessert, name='dessert'),

    #----------------requests----------------
    path('searchRecipe/', views.searchRecipe, name='searchRecipe'),
    path('loadRecipe/', views.loadRecipe, name='loadRecipe'),

    # ------------- breakfast pages -------------
    path('Breakfast-Casserole/',views.breakfastCasserole, name='breakfast-casserole'),

    # ------------- lunch pages -------------
    path('Mac-and-Cheese/',views.macAndCheese, name='mac-and-cheese'),
    path('Buffalo-Chicken-Paninis/',views.bCP, name='buffalo-chicken-paninis'),

    # ------------- beef pages -------------
    path("Granny's-Taco-Soup/",views.tacoSoup, name='grannys-taco-soup'),

    # ------------- chicken pages -------------
    path('Tuscan-Chicken/',views.tuscChick, name='tuscan-chicken'),
    path('Chicken-Tortellini/',views.chickTortel, name='chicken-tortellini'),
    path("Mom's-King-Ranch-Casserole/",views.kRC, name='kRC'),
    path('Teriyaki-Chicken/',views.teriakiChick, name='teriakiChick'),
    path("Emily's-Honey-Garlic-Chicken/",views.hGC, name='hGC'),

    # ------------- italian sausage pages -------------
    path('Mendicino-Pasta/',views.mendicino, name='mendicino'),

    # ------------- snack pages -------------


    # ------------- dessert pages -------------
    path("Mom's-Kitchen-Sink-Cookies/",views.kSC, name='kSC'),
    path("Reese's-Cheesecake-Brownies/",views.rCB, name='rCB'),

]
