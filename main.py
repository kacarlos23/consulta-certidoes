from utils import utils, selenium_utils
from time import sleep

def main():

    cadastro_corrigido, tipo = utils.analise_cadastro()
    print(f'N° de cadastro: {cadastro_corrigido}\nTipo de cadastro: {tipo}')

    while True:

        opcao = utils.menu_certidoes(tipo)

        if opcao == '0':
            print('Encerrando programa...')
            break
        else:
            ...

if __name__ == '__main__':
    main()