from django.urls import path

from . import views

app_name = 'plants'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('details/<int:pk>', views.DetailView.as_view(), name='detail'),
]