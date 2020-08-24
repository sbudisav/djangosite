from django_seed import Seed 
from .models import UserProfile
seeder = Seed.seeder()


seeder.add_entity(UserProfile, 5, {
  'username': lambda x: random.faker.name(),
  'password': 'nomiss11',
})
seeder.execute()
