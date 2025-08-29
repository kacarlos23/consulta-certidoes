import re
from time import sleep

def corrige_cad(cad):
    cad = re.sub(r'[^/d]', '', cad)

    return cad

def solicitar_e_processar_cnpj():
    cnpj = input('Digite o CNPJ: ')
    print('-> Processando CNPJ...')
    print(f'CNPJ após o processamento: {corrige_cad(cnpj)}')

def solicitar_e_processar_cpf():
    print('-> Processando CPF...')
    cpf = input('Digite o CPF: ')
    print(f'CPF após o processamento: {corrige_cad(cpf)}')