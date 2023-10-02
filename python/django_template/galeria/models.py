from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class Fotografia(models.Model):
    class Tipos(models.TextChoices):
        NEBULOSA = 'NB', _('Nebulosa')
        ESTRELA = 'ES', _('Estrela')
        GALAXIA = 'GA', _('Galáxia')
        PLANETA = 'PL', _('Planeta')

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    categoria = models.CharField(max_length=2, choices=Tipos.choices, default='')
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now(), blank=False)
    def __str__(self):
        return self.nome