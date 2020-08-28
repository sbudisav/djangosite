from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserProfile, UserPlant, FollowedUser
from posts.models import Post, Comment

# Create your tests here.

class ProfileModelTests(TestCase):

  def setUp(self):
    user1 = User.objects.create_user(username="user1", password="password")
    user2 = User.objects.create_user(username="user2", password="password")
    user3 = User.objects.create_user(username="user3", password="password")

  def test_profile_autocreate(self):
    user1 = User.objects.get(username="user1")
    user_profile = UserProfile.objects.get(user=user1)
    self.assertTrue(user1.userprofile)
    self.assertEqual(user_profile.user, user1)
    self.assertEqual(user1.userprofile, user_profile)

  def test_index(self):
    c = Client()
    c.post('/profiles/login/', {'username':'user1', 'password':'password'})
    response = c.get('/profiles/user_index')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context['users'].count(), 2)

  def test_profile_view(self):
    user1 = User.objects.get(username="user1")
    c = Client()
    response = c.get(f"/profiles/user/{user1.id}")
    self.assertEqual(response.status_code, 200)

  def test_follow_doesnt_reciprocate(self):
    user1 = User.objects.get(username="user1")
    user2 = User.objects.get(username="user2")
    user1.userprofile.start_following(user2)
    self.assertIn(user1.following, user2)
    self.assertTrue(user1.following)

