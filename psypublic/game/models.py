# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.validators import MaxValueValidator

class GameAdmin(admin.ModelAdmin):
    list_display = ('game_id','players', 'main_iteration', 'point_calc_public','point_calc_private')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user','gamePlay', 'total_donate', 'finished')

# Create your models here.
class Game(models.Model):
    def __str__(self):
        return 'Game : {}'.format(self.game_id)

    token_choices = (
        ('t','토큰'),
        ('c','사이버머니'),
        ('p','점수')
    )

    game_id = models.IntegerField(primary_key=True)
    players = models.IntegerField(default=4)

    practice_iteration = models.IntegerField(default=5,validators=[MaxValueValidator(100)])

    main_iteration = models.IntegerField(default=10,validators=[MaxValueValidator(100)])

    token_type = models.CharField(max_length=1,choices=token_choices)
    token_given = models.IntegerField(default=10000)

    point_calc_public = models.IntegerField(default=2)
    point_calc_private = models.IntegerField(default=3)

    reward_On_Off = models.BooleanField(default=False)
    wait_time = models.IntegerField(default=10)

    feedback_my_donate_public = models.BooleanField(default=False)
    feedback_other_donate_public = models.BooleanField(default=False)
    feedback_my_only = models.BooleanField(default=False)
    feedback_my_public = models.BooleanField(default=False)
    feedback_my_total = models.BooleanField(default=False)

class Player(models.Model):
    def __str__(self):
        return 'Player : {}'.format(self.user)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gamePlay = models.ForeignKey(Game)
    total_donate = models.CharField(max_length=10,default="",blank=True)

    all_donate_list = models.CharField(max_length=500,default="",blank =True)

    finished = models.BooleanField(default=False)
