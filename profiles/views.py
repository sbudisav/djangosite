from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator

from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST

from .forms import UserRegisterForm, UserUpdateForm
from .models import UserProfile, UserPlant, FollowedUser
from posts.models import Post, Comment

class UserIndex(generic.ListView):
  model = UserProfile
  template_name = 'profiles/user_index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_profile = get_object_or_404(UserProfile, user=self.request.user)
    context['users'] = UserProfile.objects.exclude(user__in=user_profile.following.all()).exclude(user=self.request.user)
    context['following'] = user_profile.following
    return context

class ProfileView(generic.DetailView):
  model = UserProfile
  context_object_name = 'user_profile'
  template_name = "profiles/user.html"

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    user = get_object_or_404(User, id=self.kwargs['pk'])
    context['user_plants'] = UserPlant.objects.filter(user=user)
    context['posts'] = Post.objects.filter(author=user)
    return context

class HomePageView(generic.DetailView):
  model = UserProfile
  template_name='profiles/home.html'
  context_object_name = 'user_profile'

  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user
    context['user'] = user
    context['posts'] = Post.objects.filter(author=user.id)
    context['user_plants'] = UserPlant.objects.filter(user=user)
    return context

class ProfileUpdateView(generic.edit.UpdateView):
  model = UserProfile
  fields = ['profile_image', 'about', 'requires_comment_validation', 'zipcode']
  success_url = reverse_lazy('profiles:redirect_home')

class UserPlantUpdateView(generic.edit.UpdateView):
  model = UserPlant
  fields = ['nickname', 'userplant_image']
  # Still needs sunlight that it's getting, need to migrate
  success_url = reverse_lazy('profiles:redirect_home')

class UserAddPost(generic.edit.CreateView):
  model = Post
  fields = ['title', 'text', 'post_image']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  success_url = reverse_lazy('profiles:redirect_home')

def register(request):
  if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          messages.success(request, f'Your account has been created! You are now able to log in')
          return redirect('profiles:login')
  else:
      form = UserRegisterForm()
  return render(request, 'profiles/register.html', {'form': form})

def redirect_to_homepage(request):
  user = request.user
  return HttpResponseRedirect(reverse('profiles:home', args=(user.id,)))

@login_required
@require_POST
def follow_user_update(request):
  user_id = request.POST.get('id')
  action = request.POST.get('action')
  if image_id and action:
    try:
      image = Image.objects.get(id=image_id)
      if action == 'follow':
        image.users_like.add(request.user)
      else:
        image.users_like.remove(request.user)
        return JsonResponse({'status':'ok'})
    except:
      pass
      return JsonResponse({'status':'ko'})