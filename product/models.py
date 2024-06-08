from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='characters/')

    def __str__(self):
        return self.name

class Rarity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
    skill_point = models.PositiveIntegerField(default=0)
    att_point = models.PositiveIntegerField(default=0)
    def_point = models.PositiveIntegerField(default=0)
    skill_type = models.ForeignKey(Character, on_delete=models.CASCADE, null=True, blank=True)
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    mana_point = models.PositiveIntegerField(blank=True,null=True )
    skill = models.ManyToManyField(User, related_name='player_skill', null=True, blank=True)

    def __str__(self):
        return self.name

class Rank(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ranks/', null=True, blank=True)
    rank = models.PositiveIntegerField(default=0)
    player_type = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)
    points = models.PositiveIntegerField(default=0)
    skill_point = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name

class Player_rank(models.Model):
    name = models.CharField(max_length=100)
    point = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name

class Player_detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    player_rank = models.ForeignKey(Player_rank, on_delete=models.CASCADE, null=True, blank=True)
    hp = models.PositiveIntegerField(default=100)
    mana = models.PositiveIntegerField(default=100)

    def __str__(self):
        return str(self.user)
    



    
    


