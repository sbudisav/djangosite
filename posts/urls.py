from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('update/<int:pk>', views.UserPostUpdateView.as_view(template_name='posts/update_post.html'), name='update_post'),
    path('like/', views.post_like, name='like'),
]