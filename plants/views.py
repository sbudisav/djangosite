from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import Plant
from profiles.models import UserPlant


class IndexView(generic.ListView):
  model = Plant
  template_name = 'plants/index.html'
  context_object_name = 'plants'

  def add_userplant(self, plant):
    Plant.add_plant(self.request.user, plant)
    # Still need to go to the model with an id. 
    return reverse_lazy('profiles:userplant_update')

class DetailView(generic.DetailView):
  model = Plant
  template_name='plants/detail.html'
  context_object_name = 'plant'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user
    context['user'] = user
    context['user_plants'] = UserPlant.objects.filter(user=user).filter(plant=self.kwargs['pk'])
    return context