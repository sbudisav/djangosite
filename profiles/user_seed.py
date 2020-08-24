from django_seed import Seed 

seeder = Seed.seeder()

from .models import UserProfile, UserPlant, FollowedUser