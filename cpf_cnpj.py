from validate_docbr import CPF, CNPJ

class CpfCnpj:

    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento.lower()
        documento = str(documento)

        if self.tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CNPJ inválido")

        elif self.tipo_documento == 'cnpj':
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido")

        else:
            raise ValueError("CPF inválido!!!")


    def __str__(self):

        if self.tipo_documento == 'cpf':
            return self.__format_cpf()

        elif self.tipo_documento == 'cnpj':
            return self.__format_cnpj()


    def cnpj_eh_valido(self,cnpj):

        if len(cnpj)==14:
            validador = CNPJ()
            return validador.validate(cnpj)

        else:
            raise ValueError('Quantdades dígitos inválidos')


    def __format_cnpj(self):

        mascara = CNPJ()
        return mascara.mask(self.cnpj)


    def cpf_eh_valido(self, cpf):

        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)

        else:
            raise ValueError('Quantdades dígitos inválidos')


    def __format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)