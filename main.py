from validate_docbr import CNPJ
from cpf_cnpj import Documento


documento = 353798380001124

cnpj_exemplo = Documento.cria_documento(documento)

print(cnpj_exemplo)

