from django.urls import path
from . import views

urlpatterns = [
    #----------------Pages----------------
    path('',views.home, name='home'),
    path('library/',views.library, name='library'),
    path('login/',views.login, name='login'),
    path('forgotpassword/',views.forgotpassword, name='forgotpassword'),
    path('signup/',views.signup, name='signup'),
    path('terms/',views.terms, name='terms'),
    path('home/',views.home, name='home'),

    #----------------requests----------------
    path('process_string/', views.process_string, name='process_string'),
    path('login_info/', views.login_info, name='login_info'),
]
