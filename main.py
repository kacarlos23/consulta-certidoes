from utils import utils, selenium_utils
from time import sleep

def main():

    cadastro_corrigido, tipo = utils.analise_cadastro()
    print(f'\nN° de cadastro: {cadastro_corrigido}\nTipo de cadastro: {tipo}\n')

    while True:

        opcao = utils.menu_certidoes(tipo, cadastro_corrigido)

        if opcao == '0':
            print('Encerrando programa...')
            break

        if tipo == 'CNPJ':
            if opcao == '1':
                link = utils.certidoes['CONSOLIDADA']['link']
                selenium_utils.iniciar_navegacao(link, cadastro_corrigido)

        elif tipo == 'CPF':
            if opcao == '1':
                link = utils.certidoes['INIDONEIDADE']['link']
                selenium_utils.iniciar_navegacao(link, cadastro_corrigido)
            if opcao == '2':
                link = utils.certidoes['IMPROBIDADE']['link']
                selenium_utils.iniciar_navegacao(link, cadastro_corrigido)
            if opcao == '3':
                link = utils.certidoes['CEIS']['link']
                selenium_utils.iniciar_navegacao(link, cadastro_corrigido)

if __name__ == '__main__':
    main()