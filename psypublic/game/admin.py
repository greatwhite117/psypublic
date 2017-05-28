from django.contrib import admin
from .models import Game, Player
from .models import GameAdmin,PlayerAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)