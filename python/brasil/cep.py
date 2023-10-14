import re
import requests

class BuscaEndereco:
    def __init__(self, cep):
        self.valida_cep(cep)
        self._cep = cep
        self._info = self.retorna_dict()

    def __str__(self):
        return 'CEP: {}, Bairro: {}, Cidade: {}, Estado: {}'.format(
            self._info['cep'],
            self._info['bairro'],
            self._info['localidade'],
            self._info['uf'],
        )
    
    def valida_cep(self, cep):
        padrao_cep = '([0-9]{5})([0-9]{3})'
        match = re.match(padrao_cep, cep)
        if len(cep) != 8 or not match:  # Esse "not match" garante que não é alfanumérico.
            raise ValueError('CEP inválido.')
        
    def formata_cep(self):  # Método desnecessário após receber o dict da API.
        padrao_cep = '([0-9]{5})([0-9]{3})'
        match = re.match(padrao_cep, self._cep)  # Poderia utilizar o fatiamento simples de strings, mas usei regex para praticar.
        cep_formatado = '{}-{}'.format(
            match.group(1),
            match.group(2)
        )
        return cep_formatado
    
    def retorna_dict(self):
        r = requests.get('https://viacep.com.br/ws/{}/json/'.format(self._cep))
        return r.json()