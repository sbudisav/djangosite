from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import UserProfile, UserPlant
from posts.models import Post, Comment

class HomeView(generic.ListView):
  model = UserProfile
  template_name = 'profiles/home.html'
  context_object_name = 'homepage'

class FeedView(generic.ListView):
  model = Post
  template_name = 'profiles/feed.html'
  context_object_name = 'posts'
  paginate_by = 10

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('published_dt')

class UserView(generic.ListView):
  # Displays username, picture, their userplants, blog posts
  model = User
  template_name = 'profiles/user.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    context['user'] = user
    # context['user_profile'] = UserProfile.objects.filter(user=user)
    context['user_plants'] = UserPlant.objects.filter(user=user)
    context['posts'] = Post.objects.filter(author=user)
    return context
  