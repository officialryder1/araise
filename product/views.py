from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Player_detail, Player_rank, Rank, Rarity, Skill, Character

import time

def home(request):
    character = Character.objects.all()
    content = {
        'character':character
    }
    return render(request, 'product/index.html', content)


def get_character(request, pk):
    character = Character.objects.get(pk=pk)
    skill = Skill.objects.all()
    request.session['product_id'] = pk
    content = {
        'cha':character,
        'skill':skill
    }
    return render(request, 'partials/character_info.html', content)

def add_skill(request, pk):
    user = request.user
    character= request.session.get('product_id')
    get_character = Character.objects.get(id=character)
    print(get_character)
    skil = get_object_or_404(Skill, id=request.POST.get('skill_id'))

    added = False
    if skil.skill.filter(id=user.id).exists():
        skil.skill.remove(request.user)
        added = False
        return HttpResponse('<button class="button is-primary has-text-primary-light" hx-post="{% url "add-skill" skill.pk %}" hx-swap="outerHTML" name="skill_id" value="{{skill.pk}}">Add</button>')
    else:
        skil.skill.add(request.user)
        return HttpResponse('<button class="button is-danger has-text-primary-light" hx-post="{% url "add-skill" skill.pk %}" hx-swap="outerHTML" name="skill_id" value="{{skill.pk}}">Added</button>')
        added = True

def create_player(request):
    user = request.user
    character= request.session.get('product_id')
    get_character = Character.objects.get(id=character)
    if Player_detail.objects.filter(user=request.user).exists():
        return redirect('/')
    else:
        create = Player_detail.objects.create(user=request.user, character=get_character, player_rank=5)
        create.save()
        return redirect('profile')

def profile(request):
    user = request.user
    skill = Skill.objects.filter(skill=user)
    skill_length = Skill.objects.filter(skill=user).count()
    player_detail = Player_detail.objects.get(user=user)
    player_rank = Player_rank.objects.all()
    rank = Rank.objects.all()
    rarity = Rarity.objects.all()
    

    content = {
        'skill':skill_length,
        'player':player_detail,
        'card':skill,

    }
    return render(request, 'product/profile.html', content)

# write me a hello world.