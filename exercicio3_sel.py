from selenium import webdriver
from selenium.webdriver.common.by import By


navegador = webdriver.Chrome()
navegador.get("https://www.timeanddate.com/weather/brazil/sao-paulo")


temp = navegador.find_element(By.CLASS_NAME, "h2").text
print(f"Temperatura atual na cidade de São Paulo: {temp}")