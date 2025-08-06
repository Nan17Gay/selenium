from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://books.toscrape.com/")

titulos = navegador.find_elements(By.CSS_SELECTOR, ".product_pod h3 a")
preco = navegador.find_elements(By.CLASS_NAME, "price_color")

for i in range(min(5, len(titulos))):
    print(titulos[i].text)
    print(f"- {preco[i].text}")
    print()
    print()