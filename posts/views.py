from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.http import require_POST

from .models import Post

class UserPostUpdateView(generic.edit.UpdateView):
  model = Post
  fields = ['title', 'text', 'post_image']
  success_url = reverse_lazy('profiles:redirect_home')

@login_required
@require_POST
def post_like(request):
  post_id = request.POST.get('id')
  action = request.POST.get('action')
  if post_id and action:
    try:
      post = Post.objects.get(id=post_id)
      if action == 'like':
        post.user_likes.add(request.user)
      else:
        post.user_likes.remove(request.user)
        return JsonResponse({'status':'ok'})
    except:
      pass
      return JsonResponse({'status':'ko'})
