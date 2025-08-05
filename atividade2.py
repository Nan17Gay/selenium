from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura o navegador
options = Options()
options.headless = False
navegador = webdriver.Chrome(options=options)

# Abre o YouTube
navegador.get("https://www.youtube.com")
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)

# Busca o vídeo
campo_busca = navegador.find_element(By.NAME, "search_query")
tema = "Gabriela Performance Video | KATSEYE"
campo_busca.send_keys(tema)
campo_busca.send_keys(Keys.ENTER)

# Espera os resultados
WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.ID, "video-title"))
)

titulos = navegador.find_elements(By.ID, "video-title")
print(f"\n🎧 Resultados para: {tema}\n")
for i in range(5):
    print(f"{i+1}. {titulos[i].text}")

# Clica no primeiro vídeo
titulos[0].click()

# Espera o player do YouTube carregar
try:
    WebDriverWait(navegador, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ytp-time-duration"))
    )
    duracao_elemento = navegador.find_element(By.CLASS_NAME, "ytp-time-duration")
    duracao_texto = duracao_elemento.text  # Exemplo: "4:03" ou "1:02:15"

    # Suporte para vídeos maiores que 1 hora
    partes = duracao_texto.split(":")
    if len(partes) == 2:
        minutos, segundos = map(int, partes)
        duracao_segundos = minutos * 60 + segundos
    elif len(partes) == 3:
        horas, minutos, segundos = map(int, partes)
        duracao_segundos = horas * 3600 + minutos * 60 + segundos
    else:
        duracao_segundos = 60  # tempo padrão de segurança

    print(f"\n⏳ Duração detectada: {duracao_texto} ({duracao_segundos} segundos)")
    time.sleep(duracao_segundos + 3)  # espera o vídeo acabar

except Exception as e:
    print(f"⚠️ Erro ao detectar duração: {e}")
    print("⏱️ Usando tempo padrão de 60 segundos.")