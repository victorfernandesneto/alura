from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self._momento_cadastro = datetime.today()

    def __str__(self):
        return 'Cadastro realizado em {}.'.format(
            self.hora_formatada()
            )
    
    def hora_formatada(self):
        return datetime.strftime(
            self._momento_cadastro,
            '%d/%m/%Y, %H:%M'
            )
    
    def tempo_de_cadastro(self):
        tempo_de_cadastro = datetime.today() - self._momento_cadastro
        return tempo_de_cadastro