from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('user/<int:pk>', views.UserView.as_view(), name='view_user'),
]