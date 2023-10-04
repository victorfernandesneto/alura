from django.contrib import admin
from apps.galeria.models import Fotografia


@admin.register(Fotografia)
class Fotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada', 'usuario')
    list_display_links = ['nome']
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario')
    list_editable = ('publicada',)
    list_per_page = 10