from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import Post

class IndexView(generic.ListView):
  model = Post
  template_name = 'posts/index.html'