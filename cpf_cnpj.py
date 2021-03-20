from validate_docbr import CPF, CNPJ

class Documento(): #classe factory
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError ('Quantidade de dígitos incorreta!!!')

class DocCpf():
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento

        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.__format()

    def valida(self, documento):

        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)

        else:
            raise ValueError('Quantdades dígitos inválidos')

    def __format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj():
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ errado !!!")

    def __str__(self):
        return self.__format_cnpj()

    def valida(self, documento):

        if len(documento)==14:
            validador = CNPJ()
            return validador.validate(documento)

        else:
            raise ValueError('Quantdades dígitos inválidos')

    def __format_cnpj(self):

        mascara = CNPJ()
        return mascara.mask(self.cnpj)

