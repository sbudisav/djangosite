from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

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

def redirect_to_homepage(request):
  user = request.user
  return HttpResponseRedirect(reverse('profiles:home', args=(user.id,)))
  # return redirect('profiles:home', pk=user.id)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

# @login_required()
class HomePageView(generic.DetailView):
  model = User
  template_name='profiles/home.html'

  # def get_queryset(self):
  #   user = request.user
  #   return Post.objects.filter(author=user).order_by('published_dt')
    # Need to configure queryset properly

  # def get_context_data(self, *args, **kwargs):
  #   context = super(HomePageView, self).get_context_data(*args, **kwargs)
  #   context['user_plants'] = UserPlant.objects.filter(user=User.id)
  #   return context

  # def get_queryset(self):
  #   current_user_friends = self.request.user.friends.values('id')
  #   sent_request = list(Friend.objects.filter(user=self.request.user).values_list('friend_id', flat=True))
  #   users = User.objects.exclude(id__in=current_user_friends).exclude(id__in=sent_request).exclude(id=self.request.user.id)
  #   return users


def profile(request, **kwargs):
  user = get_object_or_404(User, username=kwargs.get('username'))
  context = {
    'user_profile':UserProfile.objects.get(user=user),
    'user_plants':UserPlant.objects.filter(user=user),
    'posts':Post.objects.filter(author=user)
    }
  return render(request, 'profiles/user.html', context)

def login(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  user = authenticate(request, username=username, password=password)
  if user is not None:
      login(request, user)
      # Redirect to a success page.
      return redirect('profiles:home', user.id)
  else:
      # Return an 'invalid login' error message.
      return redirect('plants:home')
  return render(request, 'profiles/login.html')