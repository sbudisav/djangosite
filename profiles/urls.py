from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('feed/<str:username>', views.FeedView.as_view(), name='feed'),
    path('user/<slug:pk>', views.UserView.as_view(), name='user'),
    path('profile/<str:username>', views.profile, name='profileview')
]