import requests
import os
import sys


def main(args):
    cep = args[1]
    if len(cep) != 8:
        print('Quantidade de dígitos inválida!')
        exit()

    r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    data = r.json()

    if 'erro' not in data:
        print('O CEP "{}" foi encontrado para consulta:\n'.format(cep))
        print('CEP:         {}'.format(data['cep']))
        print('Logradouro:  {}'.format(data['logradouro']))
        print('Bairro:      {}'.format(data['bairro']))
        print('Localidade:  {}'.format(data['localidade']))
        print('UF:          {}'.format(data['uf']))
        print('DDD:         {}\n'.format(data['ddd']))
        # print('\n')
    else:
        print('O CEP "{}" foi encontrado para consulta!'.format(cep))

    return 0


if __name__ == '__main__':
    os.system('cls || clear')
    sys.exit(main(sys.argv))
