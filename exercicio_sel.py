from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://quotes.toscrape.com")

frases = navegador.find_elements(By.CLASS_NAME, "text")
autores = navegador.find_elements(By.CLASS_NAME, "author")

for i in range(len(frases)):
    print(frases[i].text)
    print(f"- {autores[i].text}")
    print()
    print()