from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  user_likes = models.ManyToManyField(User, related_name='posts_liked', blank=True)
  post_image = models.ImageField(upload_to='post_picture', blank=True)
  created_dt = models.DateTimeField(default=timezone.now)
  published_dt = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_dt = timezone.now()
    self.save()

  def save(self):
    super().save()
    if self.post_image:
      img = Image.open(self.post_image.path)
      if img.height > 300 or img.width > 300:
          output_size = (300, 300)
          img.thumbnail(output_size)
          img.save(self.post_image.path)    

  def __str__(self):
      return f'{self.title} - {self.author}'

class Comment(models.Model):
  post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  approved_comment = models.BooleanField(default=False)

  def approve(self):
    self.approved_comment = True
    self.save()

  def __str__(self):
    return f'{self.author} - RE: {self.post.title} OP: {self.post.author} '