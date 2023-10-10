from django.contrib import admin
from apps.framedata.models import Character, Move

@admin.register(Character)
class Characters(admin.ModelAdmin):
    list_display = ('id', 'character_name')
    list_display_links = ['character_name']
    search_fields = ('character_name',)
    list_per_page = 10

@admin.register(Move)
class Moves(admin.ModelAdmin):
    list_display = ['move_name', 'character']
    list_display_links = ['move_name']
    search_fields = ('character',)
    list_filter = ['character']
    list_per_page = 100