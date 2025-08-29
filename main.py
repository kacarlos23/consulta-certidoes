from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils import utils, selenium_utils as slm
from time import sleep

def exibir_menu():
    print("====================================")
    print("   SELECIONE O TIPO DE DOCUMENTO   ")
    print("====================================")
    print("1. CNPJ (Pessoa Jurídica)")
    print("2. CPF (Pessoa Física)")
    print("====================================")

# links
CONSOLIDADA = "https://certidoes-apf.apps.tcu.gov.br/"
INIDONEIDADE = "https://contas.tcu.gov.br/ords/f?p=1660:3:108728587479017::::P3_TIPO_RELACAO:INIDONEO"
IMPROBIDADE = "https://www.cnj.jus.br/improbidade_adm/consultar_requerido.php"
CEIS = "https://certidoes.cgu.gov.br/"

# loop que verifica se a pessoa escolheu apenas 1 ou 2
while True:

    exibir_menu()
    fis_jur = int(input("Digite a sua opção (1 ou 2): "))

    if fis_jur == 1:
        print('Você escolheu a opção 1. CNPJ (Pessoa Jurídica)')
        utils.solicitar_e_processar_cnpj()
        break
    elif fis_jur == 2:
        print('Você escolheu a opção 2. CPF (Pessoa Física)')
        utils.solicitar_e_processar_cpf()
        break
    else:
        print("\n[ERRO] Opção inválida! Por favor, tente novamente.\n")


# inicia o navegador
""" driver = webdriver.Chrome()

''' ===== CONSOLIDADA ====='''

# site de Consulta Consolidada de Pessoa Jurídica
driver.get(CONSOLIDADA)

# seleciona caixa e insere dados
search_box = slm.wait_for_presence(driver, By.ID, 'numero-cnpj')
search_box.send_keys(cad + Keys.RETURN)

# botao pra baixar certidão
button = slm.wait_for_clickable(driver, By.XPATH, '//*[@id="app"]/div/div/main/main/div[1]/div[2]/div/div/div[2]/div[3]/div/button')
button.click() """

'''===== IMPROBIDADE ====='''

""" driver.get(improbidade)

botao_selecionar = slm.wait_for_clickable(driver, By.ID, 'tipoPessoaFisica')
botao_selecionar.click()
sleep(.7)

search_box = slm.wait_for_presence(driver, By.NAME, 'num_cpf_cnpj')
search_box.send_keys(cad)
sleep(5)

captcha = driver.find_elements(By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")

if captcha:
    print("⚠️ CAPTCHA detectado! Resolva manualmente...")
    input("Pressione Enter depois de resolver.")
else:
    print("✅ Sem CAPTCHA")

btn_pesquisar = driver.find_element(By.ID, 'btnPesquisarRequerido')
btn_pesquisar.click() """

sleep(5)

#driver.quit()