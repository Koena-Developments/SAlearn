from django.urls import path 
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('login', views.login_view, name='login_page')
    # path('nav', views.navigation, name="nav"),
]