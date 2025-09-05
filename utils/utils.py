import re
from time import sleep
import os

# lista de todas as certidoes e os dados delas
certidoes = {
    'TCU_CONSOLIDADA': {
        'link': 'https://certidoes-apf.apps.tcu.gov.br/',
        'orgao': 'Tribunal de Contas da União',
        'descricao': 'Consulta consolidada de pessoa jurídica.'
    },
    'TCU_INIDONEIDADE': {
        'link': 'https://contas.tcu.gov.br/ords/f?p=1660:3:114749951000279::::P3_TIPO_RELACAO:INIDONEO',
        'orgao': 'Tribunal de Contas da União',
        'descricao': 'Consulta Certidão Inidôneos.'
    },
    'CNJ_IMPROBIDADE': {
        'link': 'https://www.cnj.jus.br/improbidade_adm/consultar_requerido.php',
        'orgao': 'Conselho Nacional de Justiça',
        'descricao': 'Consulta Certidão Improbidade Administrativa.'
    },
    'CGU_CEIS': {
        'link': 'https://certidoes.cgu.gov.br/',
        'orgao': 'Controladoria Geral da União',
        'descricao': 'Consulta Certidões CEIS, CNEP e CEPIM.'
    }
}

def corrige_cad(cad):
    cad_corrigido = re.sub(r'[^\d]', '', cad)
    return cad_corrigido

def analise_cadastro():

    while True:
        cadastro = input('Digite o CPF / CNPJ: ')
        cadastro_corrigido = corrige_cad(cadastro)
        len_cad = len(cadastro_corrigido)

        if len_cad == 11:
            msg = f'Cadastro de CPF. {len_cad} numeros foram inseridos'
            print(msg)
            return cadastro_corrigido, 'CPF'
        elif len_cad == 14:
            msg = f'Cadastro de CNPJ. {len_cad} numeros foram inseridos'
            print(msg)
            return cadastro_corrigido, 'CNPJ'
        else:
            msg = f'Cadastro inválido. {len_cad} números foram inseridos (esperado: 11 para CPF ou 14 para CNPJ)'
            print(msg)
            print('Tente novamente.\n')


def menu_certidoes(tipo):
    print("====================================")
    print(f"   MENU PARA {tipo}   ")
    print("====================================")
    
    if tipo == 'CPF':
        print('''====================================       
SELECIONE O TIPO DE CERTIDÃO
====================================       
1. TCU INIDONEIDADE
2. CNJ IMPROBIDADE (indisponível)
3. CGU CEIS (indisponível)
4. OUTRAS (indisponível)
0. Sair
====================================''')
        
    if tipo == 'CNPJ':
        print('''====================================       
SELECIONE O TIPO DE CERTIDÃO
====================================       
1. TCU INIDONEIDADE
2. OUTRAS (indisponível)
0. Sair
====================================''')

    opcao = input('Escolha uma opção: ')
    return opcao