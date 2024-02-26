from django.urls import path 
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_page'),
    path('', views.hello_world, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    # path('nav', views.navigation, name="nav"),
]