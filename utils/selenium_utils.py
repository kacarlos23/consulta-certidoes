from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def wait_for_presence(driver, by: By, locator: str, timeout: int = 10):
    """
    Espera até que o elemento esteja presente no DOM.
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, locator))
    )

def wait_for_visible(driver, by: By, locator: str, timeout: int = 10):
    """
    Espera até que o elemento esteja visível na página.
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, locator))
    )

def wait_for_clickable(driver, by: By, locator: str, timeout: int = 10):
    """
    Espera até que o elemento esteja clicável.
    """
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, locator))
    )

def aguardar_captcha():
    print("\n⏳ Aguardando resolução do CAPTCHA...")
    print("💡 Dica: Resolva o captcha no navegador e depois volte aqui")
    
    # Pausa para usuário resolver
    input("📌 Pressione ENTER quando terminar de resolver o captcha: ")
    
    # Pequena pausa para garantir que a página processou
    sleep(2)
    
    print("✅ Continuando execução...")
    return True

''' 
Funções de emissão de certidões referentes a União
'''

def navegacao_federal(driver, cadastro):
    informa_cnpj = wait_for_clickable(driver, By.NAME, 'niContribuinte')
    informa_cnpj.send_keys(cadastro)

    consultar_certidao = wait_for_clickable(driver, By.XPATH, '/html/body/app-root/mf-portal-layout/portal-main-layout/div/main/ng-component/ng-component/app-coleta-parametros-pj/app-coleta-parametros-template/form/div[2]/div[2]/button[1]')
    consultar_certidao.click()

    consultar_certidao_2 = wait_for_clickable(driver, By.XPATH, '/html/body/app-root/mf-portal-layout/portal-main-layout/div/main/ng-component/ng-component/ng-component/app-informar-parametro-pj/app-informar-parametro/form/div[2]/button')
    consultar_certidao_2.click()

    botao_download = wait_for_clickable(driver, By.XPATH, '//*[@id="id3e716a8a0137f0"]/ngx-datatable/div/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper[1]/datatable-body-row/div[2]/datatable-body-cell[7]/div/div/button')
    botao_download.click()

def navegacao_consolidada(driver, cadastro):

    # localiza o campo do cnpj e insere o valor
    caixa_pesquisa = wait_for_presence(driver, By.ID, 'numero-cnpj')
    caixa_pesquisa.send_keys(cadastro)

    # procura e clica no botão de pesquisa
    botao_pesquisar = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/main/div[1]/div[1]/div/div/div[3]/div/div[2]/button')
    botao_pesquisar.click()

    botao_baixar_pdf = wait_for_presence(driver, By.XPATH, '//*[@id="app"]/div/div/main/main/div[1]/div[2]/div/div/div[2]/div[3]/div/button')
    botao_baixar_pdf.click()

    sleep(5)
    return True

def navegacao_inidoneidade(driver, cadastro):
    botao_opcao = wait_for_clickable(driver, By.XPATH, '//*[@id="P3_TIPO"]/div/div/div[2]/label')
    botao_opcao.click()

    caixa_pesquisa = wait_for_presence(driver, By.XPATH, '//*[@id="P3_CPF_INI"]')
    caixa_pesquisa.send_keys(cadastro)

    botao_emitir_pdf = wait_for_presence(driver, By.XPATH, '//*[@id="B12005977244035393323"]')
    botao_emitir_pdf.click()

    botao_baixar_pdf = wait_for_presence(driver, By.XPATH, '//*[@id="R2730400877670862202"]/div[2]/div[2]/div[3]/a')
    botao_baixar_pdf.click()

def navegacao_improbidade(driver, cadastro):
    # seleciona o botao para gerar CND de pessoa física
    botao_tipo = wait_for_clickable(driver, By.XPATH, '//*[@id="tipoPessoaFisica"]')
    botao_tipo.click()

    # insere o cadastro no campo de CPF
    campo_pesquisa = wait_for_presence(driver, By.XPATH, '//*[@id="num_cpf_cnpj"]')
    campo_pesquisa.send_keys(cadastro)

    # espera a pessoa resolver o codigo captcha
    aguardar_captcha()

    # clica no botão pesquisar
    botao_pesquisar = wait_for_clickable(driver, By.XPATH, '//*[@id="btnPesquisarRequerido"]')
    botao_pesquisar.click()

    # aperta em gerar CND quando o botao aparecer
    botao_gerar_cnd = wait_for_clickable(driver, By.XPATH, '//*[@id="btnCertidaoNegativa"]')
    botao_gerar_cnd.click()

def navegacao_ceis(driver, cadastro):
    botao_ente_privado = wait_for_clickable(driver, By.XPATH, '//*[@id="__BVID__20"]/div[1]/label')
    botao_ente_privado.click()

    botao_certidao = wait_for_presence(driver, By.XPATH, '//*[@id="__BVID__31"]/tbody/tr/td[1]/div/input')
    botao_certidao.click()

    campo_pesquisa = wait_for_presence(driver, By.XPATH, '//*[@id="cpfCnpj"]')
    campo_pesquisa.send_keys(cadastro)

    botao_consultar = wait_for_clickable(driver, By.XPATH, '//*[@id="consultar"]')
    botao_consultar.click()

    botao_baixar = wait_for_clickable(driver, By.XPATH, "//tr[contains(., 'Certidão Negativa Correcional')]//button[contains(., 'Certidão')]")
    botao_baixar.click()

# Inicia a navegação e chama a função específica solicitada pelo usuário

def iniciar_navegacao(link_da_certidao, cadastro):

    # inicia o navegador
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link_da_certidao)

    try:

        if 'certidoes-apf.apps.tcu.gov.br' in link_da_certidao: # chama função pra CONSOLIDADA
            return navegacao_consolidada(driver, cadastro)

        elif 'contas.tcu.gov.br' in link_da_certidao: # chama função pra INIDONEIDADE
            return navegacao_inidoneidade(driver, cadastro)
        
        elif 'cnj.jus.br' in link_da_certidao: # chama função pra IMPROBIDADE
            return navegacao_improbidade(driver, cadastro)
        
        elif 'certidoes.cgu.gov.br' in link_da_certidao: # chama função pra CEIS
            return navegacao_ceis(driver, cadastro)
        
        elif 'servicos.receitafederal' in link_da_certidao: # chama função pra FEDERAL
            return navegacao_federal(driver, cadastro)
        
    except Exception as e:
        print(f'Erro durante a automação: {e}')
        return False
    
    finally:
        sleep(5)
        driver.close()