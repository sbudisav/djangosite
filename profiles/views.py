from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile, UserPlant, FollowedUser
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

class HomePageView(TemplateView):
  @method_decorator(login_required)
  
  def get_queryset(self):
    user = request.user
    return Post.objects.filter(author=user).order_by('published_dt')

  def get_feed(self):
    user = request.user
    for followed_user in followed_user_list:
      followed_posts = Post.objects.filter(author=followed_user)
      for post in followed_posts:
        post_feed.append(post)
    paginate_by = 10

  def get_queryset(self):
    current_user_friends = self.request.user.friends.values('id')
    sent_request = list(Friend.objects.filter(user=self.request.user).values_list('friend_id', flat=True))
    users = User.objects.exclude(id__in=current_user_friends).exclude(id__in=sent_request).exclude(id=self.request.user.id)
    return users


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