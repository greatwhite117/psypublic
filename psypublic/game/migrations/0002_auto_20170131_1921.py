# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 10:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_donate', models.IntegerField()),
                ('gamePlay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='gameresult',
            name='game_id',
        ),
        migrations.RemoveField(
            model_name='gameresult',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='GameResult',
        ),
    ]
