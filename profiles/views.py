from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile, UserPlant
from posts.models import Post, Comment

def register(request):
  if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          messages.success(request, f'Your account has been created! You are now able to log in')
          return redirect('login')
  else:
      form = UserRegisterForm()
  return render(request, 'profiles/register.html', {'form': form})

# @login_required
def homepage(request):
  model = UserProfile
  # template_name = 'profiles/home.html'
  # context_object_name = 'homepage'
  # context = 'homepage'
  return render(request, 'profiles/home.html', {'homepage':homepage})

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('published_dt')

class FeedView(generic.ListView):
  model = Post
  template_name = 'profiles/feed.html'
  context_object_name = 'posts'
  paginate_by = 10
  # Get friends, grab all posts, sort by most recent


class UserView(generic.DetailView):
  # Displays username, picture, their userplants, blog posts
  model = UserProfile
  template_name = 'profiles/user.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    # context['user_profile'] = user
    context['user_profile'] = UserProfile.objects.get(user=user)
    context['user_plants'] = UserPlant.objects.filter(user=user)
    context['posts'] = Post.objects.filter(author=user)
    return context

def profile(request, **kwargs):
  user = get_object_or_404(User, username=kwargs.get('username'))
  context = {
    'user_profile':UserProfile.objects.get(user=user),
    'user_plants':UserPlant.objects.filter(user=user),
    'posts':Post.objects.filter(author=user)
    }
  return render(request, 'profiles/user.html', context)