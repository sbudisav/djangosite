from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class PublicProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='profile_pic')

  def __str__(self):
      return f'{self.user.username} Profile'

  def save(self):
      super().save()

      img = Image.open(self.image.path)

      if img.height > 300 or img.width > 300:
          output_size = (300, 300)
          img.thumbnail(output_size)
          img.save(self.image.path)

class UserPlant(models.Model):
  user = models.ForeignKey('profiles.PublicProfile', on_delete=models.CASCADE)
  plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE)
  def __str__(self):
    return f'{self.user.username}s {self.plant.name}'



class PrivateProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  zipcode = models.CharField(max_length=5)
  requires_comment_validation = models.BooleanField(default=False)