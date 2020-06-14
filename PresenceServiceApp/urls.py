from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="indexPage"),
    path('panel/', views.panel, name="panel"),
    path('register/', views.registerPage, name="registerPage"),
    path("logout/", views.logoutUser,name="Logout"),
    
]
