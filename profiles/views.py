from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile, UserPlant, Friend
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

@login_required
def homepage(request):
  model = UserProfile
  # template_name = 'profiles/home.html'
  # context_object_name = 'homepage'
  # context = 'homepage'
  return render(request, 'profiles/home.html', {'homepage':homepage})

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('published_dt')

@login_required
def feed(request):
  user = request.user
  friend_list = Friend.objects.filter(user=user)
  post_feed = []
  # Should building post feed be a function? 
  for friend in friend_list:
    friend_posts = Post.objects(filter(author=friend))
    for post in friend_posts:
      post_feed.append(post)

  # still need to filter by date
  # Posts might automatically pull in comments we will have to see
  # comments = Post.objects.get(user__username=user)
  template_name = 'profiles/feed.html'
  paginate_by = 10
  return render(request, 'profiles/feed.html', {'posts':post_feed})



  # How to define user
  # request = everything included in request when sent
  # This includes the current logged in user/session


# Had generic class based view but deleted it, as profile does
# Same thing but with more flexabilty. Should be in any git 
# Commit older than 5/7
def profile(request, **kwargs):
  user = get_object_or_404(User, username=kwargs.get('username'))
  context = {
    'user_profile':UserProfile.objects.get(user=user),
    'user_plants':UserPlant.objects.filter(user=user),
    'posts':Post.objects.filter(author=user)
    }
  return render(request, 'profiles/user.html', context)

def update_profile(request):
  model = UserProfile

