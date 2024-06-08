from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('get_character/<int:pk>/', get_character, name='character'),
    path('add_skill/<int:pk>', add_skill, name='add-skill'),
    path('create_player', create_player, name='create_player'),
    path('profile', profile, name='profile')
]

