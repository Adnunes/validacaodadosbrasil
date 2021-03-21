from acessoCep import BuscaEndereco
import requests

cep = '02022030'
objeto_cep = BuscaEndereco(cep)

a = objeto_cep.acessa_via_cep()

print(a)

'''r = requests.get('https://viacep.com.br/ws/01001000/json/')


print(r.text)'''