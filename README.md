# Validação de Números WhatsApp

Este projeto valida se números de telefone estão associados a contas do WhatsApp usando o WhatsApp Web e a biblioteca Playwright. O objetivo é qualificar leads para campanhas de marketing ou apresentações via WhatsApp.

---

## Pré-requisitos

- Certifique-se de ter uma conta no WhatsApp e acesso ao WhatsApp Web.
- **Base de Dados:** Prepare um arquivo Excel com as seguintes colunas:
  - **`id`**: Identificador único.
  - **`telefone`**: Número de telefone com código do país (ex.: `5511999999999`).

---

## Estrutura do Código

1. **Carregamento da Base de Dados:**
   - O arquivo Excel é carregado utilizando a biblioteca `Pandas`.

2. **Automação do WhatsApp Web:**
   - O navegador é aberto, e o login no WhatsApp Web é realizado.
   - Para cada número de telefone, um link de contato é acessado.
   - A presença de um campo de mensagem no WhatsApp determina se o número é válido.

3. **Resultados:**
   - A planilha é atualizada com uma nova coluna (`Whatsapp`), indicando se o número é válido ou inválido.

4. **Saída Final:**
   - A base validada é salva em um novo arquivo Excel no mesmo diretório especificado.

---

## Como Usar

1. **Configure o Caminho do Arquivo Excel:**
   - Modifique o valor da variável `arquivo_excel` no código para apontar para sua planilha de entrada.

2. **Execute o Código:**
   - Certifique-se de estar em um ambiente que suporte Python assíncrono, como Jupyter Notebook ou diretamente no terminal:
     ```bash
     python nome_do_arquivo.py
     ```

3. **Realize o Login no WhatsApp Web:**
   - O script aguardará que o QR Code seja escaneado no WhatsApp Web.

4. **Resultados:**
   - O arquivo de saída será salvo no mesmo diretório especificado no código, com os resultados de validação.

---

## Observações

- **Tempo de Validação:** Ajuste o tempo de espera (`asyncio.sleep`) no código conforme a velocidade de sua conexão.
- **Segurança:** O WhatsApp pode limitar o número de requisições em um curto período. Use o script com moderação.
- **Erro ao Validar:** Números não associados ao WhatsApp serão marcados como `Inválido` na base de dados.

---

## Melhorias Futuras

- Implementar paralelismo para aumentar a eficiência da validação.
- Adicionar tratamento de erros para cenários específicos (ex.: conexões lentas).
- Criar uma interface gráfica para facilitar a entrada e saída de dados.

---
