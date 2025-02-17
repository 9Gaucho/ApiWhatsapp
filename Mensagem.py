import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote

# Carregar os contatos do arquivo JSON
with open("contatos.json", "r", encoding="utf-8") as file:
    contatos = json.load(file)

# Configurar o driver do Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Mantém o navegador aberto após execução
driver = webdriver.Chrome(options=options)

# Acessar o WhatsApp Web
driver.get("https://web.whatsapp.com")
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//canvas')))  # Espera carregar o QR Code

input("Escaneie o QR Code e pressione Enter para continuar...")  # Aguarda login manual

# Loop para enviar mensagens
for contato in contatos:
    nome = contato.get("nome")
    telefone = contato.get("telefone")

    if not telefone:
        print(f"Telefone inválido para {nome}. Pulando...")
        continue

    mensagem = f"Olá {nome}, eu estou fazendo uma automação"
    print(f"Enviando mensagem para {telefone}...")

    # Acessar a conversa diretamente sem recarregar o WhatsApp Web
    driver.get(f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}")

    try:
        # Esperar a caixa de mensagem carregar
        input_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@title="Digite uma mensagem"]'))
        )

        # Garantir que a caixa de texto está focada
        driver.execute_script("arguments[0].focus();", input_box)

        # Digitar a mensagem com um pequeno delay para simular digitação humana
        for char in mensagem:
            input_box.send_keys(char)
            time.sleep(0.05)  # Pequeno delay entre caracteres

        time.sleep(1)  # Pequeno tempo antes do envio

        # Pressionar Enter para enviar a mensagem
        input_box.send_keys(Keys.ENTER)

        print(f"Mensagem enviada para {telefone}!")
        time.sleep(2)  # Tempo curto para evitar sobrecarga

    except Exception as e:
        print(f"Erro ao enviar mensagem para {telefone}: {e}")

print("Automação concluída! O WhatsApp Web permanecerá aberto.")
