from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_image = models.ImageField(default='default_profile.jpg', upload_to='profile_pic', blank=True)
  about = models.CharField(max_length=600, default='', blank=True)
  zipcode = models.CharField(max_length=5, default='', blank=True)
  requires_comment_validation = models.BooleanField(default=False)

  def __str__(self):
      return f'{self.user.username} Profile'

  def save(self):
    super().save()
    img = Image.open(self.user_image.path)
    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.user_image.path)

class Friend(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')

class UserPlant(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE)
  nickname = models.CharField(max_length=25, default='')
  userplant_image = models.ImageField(upload_to='userplant_pic', blank=True)

  def __str__(self):
    return f'{self.user.username}s {self.plant.name} - {self.nickname}'

  def save(self):
    super().save()
    if self.userplant_image:
      img = Image.open(self.userplant_image.path)
      if img.height > 300 or img.width > 300:
          output_size = (300, 300)
          img.thumbnail(output_size)
          img.save(self.userplant_image.path)