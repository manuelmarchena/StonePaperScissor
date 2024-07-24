from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)
    games_lost = models.IntegerField(default=0)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
    def win_percentage(self):
        if self.games_played > 0:
            return (self.games_won / self.games_played) * 100
        return 0 