from django.db import models
from django.conf import settings

# Create your models here.

class Plant(models.Model):
  name = models.CharField(max_length=80)
  bionominal = models.CharField(max_length=80)
  description = models.TextField()
  sun_pref_choices = [
      ('1', "High"),
      ('2', "Med/High"),
      ('3', "Med"),
      ('4', "Med/Low"),
      ('5', "Low"),
      ('6', "Any")]
  sun_pref = models.CharField(max_length=10, choices=sun_pref_choices)
  water_freq = models.IntegerField()
  fertilizer_freq = models.IntegerField()

  def __str__(self):
    return self.name

  # def get_absolute_url(self):
  #   return reverse("products:plant-detail", kwargs={"id": self.id})
