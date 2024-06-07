# Generated by Django 5.0.6 on 2024-06-06 17:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='characters/')),
            ],
        ),
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ranks/')),
                ('rank', models.PositiveIntegerField(default=0)),
                ('points', models.PositiveIntegerField(default=0)),
                ('skill_point', models.PositiveIntegerField(default=0)),
                ('player_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.character')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='skills/')),
                ('skill_point', models.PositiveIntegerField(default=0)),
                ('att_point', models.PositiveIntegerField(default=0)),
                ('def_point', models.PositiveIntegerField(default=0)),
                ('rarity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.rarity')),
                ('skill_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.character')),
            ],
        ),
        migrations.CreateModel(
            name='Player_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.PositiveIntegerField(default=10)),
                ('mana', models.PositiveIntegerField(default=100)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.character')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.rank')),
                ('skill', models.ManyToManyField(related_name='player_skill', to='product.skill')),
            ],
        ),
    ]