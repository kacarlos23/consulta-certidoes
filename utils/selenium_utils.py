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

def iniciar_navegacao(link_da_certidao, cadastro):

    # inicia o navegador
    driver = webdriver.Chrome()
     
    # abre o site da certidao
    driver.get(link_da_certidao)

    if link_da_certidao == 'https://certidoes-apf.apps.tcu.gov.br/':

        # localiza o campo do cnpj e insere o valor
        caixa_pesquisa = wait_for_presence(driver, By.ID, 'numero-cnpj')
        caixa_pesquisa.send_keys(cadastro)

        # procura e clica no botão de pesquisa
        botao_pesquisar = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/main/main/div[1]/div[1]/div/div/div[3]/div/div[2]/button')
        botao_pesquisar.click()

        botao_baixar_pdf = wait_for_presence(driver, By.XPATH, '//*[@id="app"]/div/div/main/main/div[1]/div[2]/div/div/div[2]/div[3]/div/button')
        botao_baixar_pdf.click()

    elif link_da_certidao == 'https://contas.tcu.gov.br/ords/f?p=1660:3:114749951000279::::P3_TIPO_RELACAO:INIDONEO':
        botao_opcao = wait_for_clickable(driver, By.XPATH, '//*[@id="P3_TIPO"]/div/div/div[2]/label')
        botao_opcao.click()

        caixa_pesquisa = wait_for_presence(driver, By.XPATH, '//*[@id="P3_CPF_INI"]')
        caixa_pesquisa.send_keys(cadastro)

        botao_emitir_pdf = wait_for_presence(driver, By.XPATH, '//*[@id="B12005977244035393323"]')
        botao_emitir_pdf.click()

        botao_baixar_pdf = wait_for_presence(driver, By.XPATH, '//*[@id="R2730400877670862202"]/div[2]/div[2]/div[3]/a')
        botao_baixar_pdf.click()

    sleep(10)

    driver.close()