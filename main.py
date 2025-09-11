from utils import utils, selenium_utils
from time import sleep

def main():

    cadastro_corrigido, tipo = utils.analise_cadastro()
    print(f'\nN° de cadastro: {cadastro_corrigido}\nTipo de cadastro: {tipo}\n')

    while True:

        opcao = utils.menu_certidoes(tipo, cadastro_corrigido)

        if opcao == '99':
            print('Encerrando programa...')
            break

        if tipo == 'CNPJ':
            if opcao == '1':
                link = utils.certidoes['CONSOLIDADA']['link']
                selenium_utils.iniciar_navegacao(link, cadastro_corrigido)
            elif opcao == '2':
                link = utils.certidoes['FEDERAL']['link']
                selenium_utils.iniciar_navegacao(link, cadastro_corrigido)
            elif opcao == '0':
                # Emitir todas as certidões de CNPJ
                for certidao in utils.certidoes_disponiveis['CNPJ']:
                    link = utils.certidoes[certidao]['link']
                    print(f"\n--- Emitindo {certidao} ---")
                    selenium_utils.iniciar_navegacao(link, cadastro_corrigido)
                    sleep(2)  # Pequena pausa entre as certidões

        elif tipo == 'CPF':
            if opcao == '1':
                link = utils.certidoes['INIDONEIDADE']['link']
                selenium_utils.iniciar_navegacao(link, cadastro_corrigido)
            elif opcao == '2':
                link = utils.certidoes['IMPROBIDADE']['link']
                selenium_utils.iniciar_navegacao(link, cadastro_corrigido)
            elif opcao == '3':
                link = utils.certidoes['CEIS']['link']
                selenium_utils.iniciar_navegacao(link, cadastro_corrigido)
            elif opcao == '0':
                # Emitir todas as certidões de CPF
                for certidao in utils.certidoes_disponiveis['CPF']:
                    link = utils.certidoes[certidao]['link']
                    print(f"\n--- Emitindo {certidao} ---")
                    selenium_utils.iniciar_navegacao(link, cadastro_corrigido)
                    sleep(2)  # Pequena pausa entre as certidões
                
if __name__ == '__main__':
    main()