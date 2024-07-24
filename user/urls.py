from django.urls import path
from .views import register
from . import views 

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.CustomLoginView.as_view() , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('user/', register, name='register'),
]
