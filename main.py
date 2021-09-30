import requests
import os

os.system('cls')

cep = input('Digite o CEP: ')
r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

data = r.json()

print('''
    CEP:            {}
    Logradouro:     {}
    Bairro:         {}
    Localidade:     {}
    UF:             {}
    DDD:            {}
'''.format(
    data['cep'],
    data['logradouro'],
    data['bairro'],
    data['localidade'],
    data['uf'],
    data['ddd']
))
