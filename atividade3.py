from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.headless = False

navegador = webdriver.Chrome(options=options)

navegador.get("https://www.google.com")

time.sleep(2)

campo_pesquisa = navegador.find_element(By.NAME, "q")

campo_pesquisa.send_keys("Ana Clara Mendes")

campo_pesquisa.send_keys(Keys.ENTER)

time.sleep(5)

navegador.quit()
