from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    pass

class Skill(models.Model):
    pass

class Rank(models.Model):
    pass

class Player_detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill, related_name='player_skill')
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    hp = models.PositiveIntegerField(default=10)
    mana = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.user


    
    


