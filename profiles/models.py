from django.db import models
from django.contrib.auth.models import User
from posts.models import Post, Comment
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from PIL import Image

class UserProfile(models.Model):
  user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, primary_key=True)
  profile_image = models.ImageField(default='default_profile.jpg', upload_to='profile_images', blank=True)
  about = models.CharField(max_length=600, default='', blank=True)
  zipcode = models.CharField(max_length=5, default='', blank=True)
  requires_comment_validation = models.BooleanField(default=False)
  # slug = models.SlugField(max_length=200, default=self.user.username)
  following = models.ManyToManyField('self', through='FollowedUser', symmetrical=False, related_name='is_following')

  def followers(self):
    users_following = FollowedUser.objects.filter(followed_user=self)
    return users_following

    # While I don't use these for following I'm keeping them incase I ever feel like trimming down the view

  def start_following(current_user, followed_user):
    # print(f"initiated start following with current user {self} and followed user {followed_user}")
    FollowedUser.objects.get_or_create(
        user=current_user,
        followed_user=followed_user)
    return

  def stop_following(current_user, followed_user):
    print(f"initiated stop following with current user {self} and followed user {followed_user}")
    FollowedUser.objects.get(
        user=current_user,
        followed_user=followed_user).delete()
    return

  def user_feed(self):
    post_feed = []
    follow_object = FollowedUser.objects.filter(user=self)
    for fo in follow_object:
      followed_posts = Post.objects.filter(author=fo.followed_user.user)
      for post in followed_posts:
         post_feed.append(post)
         # post_feed.objects.order_by('created_dt')
    return post_feed

  def get_absoloute_url(self):
    return reverse('profile_detail', kwargs={'pk': self.pk})

  def __str__(self):
    return f'{self.user.username}'

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    if self.profile_image:
      img = Image.open(self.profile_image.path)
      if img.height > 300 or img.width > 300:
          output_size = (300, 300)
          img.thumbnail(output_size)
          img.save(self.profile_image.path)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

  # Note sure if I need this receiver or if it should be in the save function above. 
  # @receiver(post_save, sender=User)
  # def save_user_profile(sender, instance, **kwargs):
  #   instance.profile.save()

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
  userplant_image = models.ImageField(upload_to='userplant_images/', blank=True)

  def __str__(self):
    return f'{self.user.username}s {self.plant.name} - {self.nickname}'

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    if self.userplant_image:
      img = Image.open(self.userplant_image.path)
      if img.height > 300 or img.width > 300:
          output_size = (300, 300)
          img.thumbnail(output_size)
          img.save(self.userplant_image.path)