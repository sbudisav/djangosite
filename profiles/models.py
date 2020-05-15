from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class UserProfile(models.Model):
  user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, primary_key=True)
  profile_image = models.ImageField(default='default_profile.jpg', upload_to='profile_pic', blank=True)
  about = models.CharField(max_length=600, default='', blank=True)
  zipcode = models.CharField(max_length=5, default='', blank=True)
  requires_comment_validation = models.BooleanField(default=False)

  following = models.ManyToManyField('self', through='FollowedUser', symmetrical=False, related_name='is_following')

  def start_following(self, followed_user):
    FollowedUser.objects.get_or_create(
        user=self,
        followed_user=followed_user)
    return

  def stop_following(self, followed_user):
    FollowedUser.objects.filter(
        user=self,
        followed_user=followed_user).delete()
    return

  def user_feed(self):
    for follow_object in self.following:
      followed_posts = Post.objects.filter(author=follow_object.followed_user)
      for post in followed_posts:
        post_feed.append(post)
    return post_feed

  def __str__(self):
    return f'{self.user.username} Profile'

  def save(self):
    super().save()
    if self.profile_image:
      img = Image.open(self.profile_image.path)
      if img.height > 300 or img.width > 300:
          output_size = (300, 300)
          img.thumbnail(output_size)
          img.save(self.profile_image.path)

class FollowedUser(models.Model):
  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  followed_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followed_user')
  # primary key is a composite key

  def __str__(self):
    return f'{self.user.user.username} follows {self.followed_user.user.username}'

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