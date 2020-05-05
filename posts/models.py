from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_dt = models.DateTimeField(default=timezone.now)
  published_dt = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_dt = timezone.now()
    self.save()

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