from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Post

class UserPostUpdateView(generic.edit.UpdateView):
  model = Post
  fields = ['title', 'text', 'post_image']
  success_url = reverse_lazy('profiles:redirect_home')
