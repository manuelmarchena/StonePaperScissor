from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from user.models import UserProfile

class Command(BaseCommand):
    help = 'Create user profiles for users without one'

    def handle(self, *args, **kwargs):
        users_without_profile = User.objects.filter(userprofile__isnull=True)
        for user in users_without_profile:
            UserProfile.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS('Successfully created profiles for users without one'))
