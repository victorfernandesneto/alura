from django.contrib import admin
from galeria.models import Fotografia


@admin.register(Fotografia)
class Fotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ['nome']
    search_fields = ('nome',)
    list_filter = ("categoria",)
    list_editable = ('publicada',)
    list_per_page = 10