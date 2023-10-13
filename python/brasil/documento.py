from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocumentoCPF(documento)
        elif len(documento) == 14:
            return DocumentoCNPJ(documento)
        else:
            raise ValueError('Documento inválido.')

class DocumentoCPF:
    def __init__(self, documento):
        self.valida_documento(documento)
        self._tipo = 'CPF'
        self._numero = documento
        
    def valida_documento(self, documento):
        cpf = CPF()
        if not cpf.validate(documento):
            raise ValueError('Documento inválido.')
        
    def formata_documento(self):
        cpf = CPF()
        return cpf.mask(self._numero)
        
    def __str__(self):
        return f'Documento número {self.formata_documento()}.'
    
class DocumentoCNPJ:
    def __init__(self, documento):
        self.valida_documento(documento)
        self._tipo = 'CNPJ'
        self._numero = documento
        
    def valida_documento(self, documento):
        cnpj = CNPJ()
        if not cnpj.validate(documento):
            raise ValueError('Documento inválido.')
        
    def formata_documento(self):
        cnpj = CNPJ()  
        return cnpj.mask(self._numero)
        
    def __str__(self):
        return f'Documento número {self.formata_documento()}.'