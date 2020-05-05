from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import PublicProfile, UserPlant, PrivateProfile
from posts.models import Post, Comment

class HomeView(generic.ListView):
  model = PublicProfile
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
  model = UserPlant
  template_name = 'profiles/user.html'
  context_object_name = 'plants'

  def get_queryset(self):
    plant_owner = get_object_or_404(User, username=self.kwargs.get('username'))
    return UserPlant.objects.filter(user=plant_owner)
  

