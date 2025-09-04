import re
from time import sleep
import os

def menu_cadastro():
    os.system('cls')
    print("====================================")
    print("   SELECIONE O TIPO DE DOCUMENTO   ")
    print("====================================")
    print("1. CNPJ - Pessoa Jurídica")
    print("2. CPF - Pessoa Física (indisponível)")
    print("====================================")

def menu_certidoes():
    print("====================================")
    print("   SELECIONE O TIPO DE CERTIDÃO   ")
    print("====================================")
    print("1. TCU CONSOLIDADA")
    print("2. TCU INIDONEIDADE (indisponível)")
    print("3. CNJ IMPROBIDADE (indisponível)")
    print("4. CGU CEIS (indisponível)")
    print("0. SAIR")
    print("====================================")

def corrige_cad(cad):
    cad_corrigido = re.sub(r'[^\d]', '', cad)

    return cad_corrigido

def solicitar_e_processar_cnpj():
    cnpj_original = input('Digite o CNPJ: ')
    print('-> Processando CNPJ...')
    sleep(2)
    os.system('cls')
    cnpj_corrigido = corrige_cad(cnpj_original)
    print(f'CNPJ após o processamento: {cnpj_corrigido}')

    return cnpj_corrigido

def solicitar_e_processar_cpf():
    cpf_original = input('Digite o CPF: ')
    print('-> Processando CPF...')
    print(2)
    os.system('cls')
    cpf_corrigido = corrige_cad(cpf_original)
    print(f'CPF após o processamento: {cpf_corrigido}')

    return cpf_corrigido