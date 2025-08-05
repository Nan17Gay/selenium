from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.headless = False

navegador = webdriver.Chrome(options=options)
navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSe1kM6GuDUR34BcH88YdKuiCcjCQVevFWhElbNLtsoBHGob2A/viewform?usp=dialog")
time.sleep(4)

# Preencher campos
campo_nome = navegador.find_element(By.XPATH, '//div[@role="listitem"][1]//input')
campo_nome.send_keys("Ana Clara")

campo_email = navegador.find_element(By.XPATH, '//div[@role="listitem"][2]//input')
campo_email.send_keys("usuariodedougl45@gmail.com")

# Clicar em Enviar
botao_enviar = navegador.find_element(By.XPATH, '//span[contains(text(), "Enviar")]/ancestor::div[@role="button"]')
botao_enviar.click()

# Espera e fecha
time.sleep(3)
navegador.quit()
