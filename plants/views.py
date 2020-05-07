from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User

from .models import Plant


class IndexView(generic.ListView):
  model = Plant
  template_name = 'plants/index.html'
  context_object_name = 'plants'