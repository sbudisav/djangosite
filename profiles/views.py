from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import PublicProfile, UserPlant, PrivateProfile
from posts.models import Post, Comment

class HomeView(generic.DetailView):
  model = PublicProfile
  template_name = 'profiles/home.html'

class FeedView(generic.ListView):
  model = Post
  template_name = 'profiles/feed.html'

class UserView(generic.DetailView):
  model = PublicProfile
  template_name = 'profiles/user'
