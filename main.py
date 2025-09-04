from utils import utils, selenium_utils
from time import sleep

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

def main():

    # loop que verifica se a pessoa escolheu apenas 1 ou 2
    while True:

        utils.menu_cadastro()
        fis_jur = input("Digite a sua opção (1 ou 2): ")

        if fis_jur == '1':
            print('Opção selecionada -> CNPJ - Pessoa Jurídica')
            cnpj_corrigido = utils.solicitar_e_processar_cnpj()
            break
        elif fis_jur == '2':
            print('Você escolheu a opção 2. CPF (Pessoa Física)')
            cpf_corrigido = utils.solicitar_e_processar_cpf()
            break
        else:
            print("\n[ERRO] Opção inválida! Por favor, tente novamente.\n")

    while True:

        utils.menu_certidoes() # exibe o menu de certidões
        escolha_certidao = input("Digite a sua opção: ")

        if escolha_certidao == '1': # caso TCU CONSOLIDADA
            certidao_escolhida = certidoes['TCU_CONSOLIDADA']['link']
            selenium_utils.iniciar_navegacao(certidao_escolhida, cnpj_corrigido)
        elif escolha_certidao == '0': # caso SAIR
            print('Encerrando programa...')
            sleep(2)
            break
        else:
            print("\n[ERRO] Opção inválida! Por favor, tente novamente.\n")

if __name__ == '__main__':
    main()