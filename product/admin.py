from django.contrib import admin
from .models import Character, Player_detail, Rank, Skill, Rarity, Player_rank

admin.site.register(Character)
admin.site.register(Player_detail)
admin.site.register(Rank)
admin.site.register(Skill)
admin.site.register(Rarity)
admin.site.register(Player_rank)
# Register your models here.

