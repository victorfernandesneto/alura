import re

class Telefone:
    def __init__(self, numero):
        self.valida_telefone(numero)
        self._numero = numero

    def __str__(self):
        return 'Número de telefone {}.'.format(
            self.formata_telefone()
        )

    def valida_telefone(self, numero):
        padrao_telefone = '([0-9]{2})?([0-9]{4,5})([0-9]{4})'
        if not re.match(padrao_telefone, numero):
            raise ValueError('Telefone inválido.')
        
    def formata_telefone(self):
        padrao_telefone = '([0-9]{2})?([0-9]{4,5})([0-9]{4})'
        mascarado = re.match(padrao_telefone, self._numero)
        if len(mascarado.group()) >= 10:
            return '({}){}-{}'.format(
                mascarado.group(1), mascarado.group(2), mascarado.group(3)
                )
        else:
            return '{}-{}'.format(
                mascarado.group(2), mascarado.group(3)
                )