import pandas as pd
from time import sleep
from playwright.async_api import async_playwright
import asyncio
import nest_asyncio

# Aplicar nest_asyncio para evitar conflitos de loops
nest_asyncio.apply()

# Inicializar listas de números válidos e inválidos
validos = []
invalidos = []

# Caminho do arquivo Excel
arquivo_excel = '/home/raspberrypi/Downloads/base_2.xlsx'

async def validar_whatsapp():
    # Carregar a base de dados
    arquivo = pd.read_excel(arquivo_excel)
    base = pd.DataFrame(arquivo)

    async with async_playwright() as p:
        # Iniciar o navegador
        browser = await p.chromium.launch(headless=False)  # Use headless=True para rodar sem interface gráfica
        context = await browser.new_context()
        page = await context.new_page()

        # Acessar o WhatsApp Web
        await page.goto('https://web.whatsapp.com/')
        print("Aguardando login no WhatsApp...")

        # Esperar que o QR code seja escaneado
        await page.wait_for_selector("#side", timeout=60000)  # Timeout de 60 segundos para login
        print("Login concluído!")

        # Iterar sobre os números de telefone
        for i, cpf in enumerate(base["cpf"]):
            telefone = base.loc[i, 'telefone']
            link = f'https://web.whatsapp.com/send?phone=+{telefone}&text='
            await page.goto(link)
            await asyncio.sleep(20)  # Aguarda carregar a página

            try:
                # Verificar se o campo de mensagem está disponível
                await page.wait_for_selector('//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p', timeout=60000)
                print(i + 1, "WhatsApp Válido")
                validos.append(telefone)
                base.loc[base["cpf"] == cpf, 'Whatsapp'] = 'Valido'

            except Exception:
                print(i + 1, "WhatsApp Inválido")
                invalidos.append(telefone)
                base.loc[base["cpf"] == cpf, 'Whatsapp'] = 'Invalido'

            # Salvar progresso a cada iteração
            base.to_excel('/home/raspberrypi/Downloads/Numeros Validados2.xlsx', index=False)

        # Encerrar o navegador
        await browser.close()

    # Exibir resultados
    print("Fim do Código")
    print("WhatsApp Válidos:", len(validos))
    print("WhatsApp Inválidos:", len(invalidos))

# Executar a função assíncrona diretamente
await validar_whatsapp()
