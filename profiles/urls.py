from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'profiles'
urlpatterns = [
    path('home/<int:pk>', views.HomePageView.as_view(), name='home'),
    path('user/<str:username>', views.profile, name='profile'),
    path('home/update/<int:pk>', views.ProfileUpdateView.as_view(template_name='profiles/profile_update.html'), name='profile_update'),
    path('home/update_plant/<int:pk>', views.UserPlantUpdateView.as_view(template_name='profiles/userplant_update.html'), name='userplant_update'),
    path('register/', views.register, name='register'),
    path('redirect_home/', views.redirect_to_homepage, name='redirect_home'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
]