from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='profile_pic')
  about = models.CharField(max_length=600)
  zipcode = models.CharField(max_length=5)
  requires_comment_validation = models.BooleanField(default=False)

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
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE)
  nickname = models.CharField(max_length=25, default='')

  def __str__(self):
    return f'{self.user.username}s {self.plant.name} - {self.nickname}'