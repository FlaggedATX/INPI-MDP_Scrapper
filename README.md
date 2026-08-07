
# INPI-MDP_Scrapper

<img src="https://github.com/user-attachments/assets/448a9786-8e03-4932-ab5f-754b64fe0588" width="700">

O **INPI-MDP_Scrapper** é uma aplicação desktop desenvolvida em Python que permite pesquisar termos específicos nas publicações mais recentes do **Instituto Nacional da Propriedade Industrial (INPI)**.

A aplicação utiliza **Selenium em modo headless** para acessar e baixar automaticamente os PDFs das publicações de:

* **Desenhos Industriais**
* **Marcas**
* **Patentes**

Após o download, os arquivos são organizados automaticamente em uma pasta criada pelo programa na área de trabalho. Em seguida, a aplicação percorre os documentos e identifica as páginas nas quais o termo pesquisado aparece.

Os PDFs nos quais o termo não é encontrado são automaticamente removidos, mantendo apenas os documentos relevantes para a pesquisa.

## Objetivo

O projeto foi desenvolvido como uma ferramenta de automação para facilitar o acompanhamento de novas publicações do INPI, reduzindo a necessidade de consultar manualmente documentos extensos em busca de termos específicos.

## Tecnologias utilizadas

* **Python**
* **PyQt5** — interface gráfica
* **Selenium** — automação e download dos documentos
* **pypdf** — extração e pesquisa de texto nos PDFs

## Funcionamento

De forma simplificada, o programa segue este fluxo:

1. Acessa o portal de publicações do INPI.
2. Identifica a publicação mais recente.
3. Baixa os PDFs de Desenhos Industriais, Marcas e Patentes.
4. Organiza os arquivos em uma pasta específica na área de trabalho.
5. Pesquisa o termo informado pelo usuário em cada documento.
6. Exibe as páginas nas quais o termo foi encontrado.
7. Remove os PDFs nos quais nenhuma ocorrência foi identificada.

## Observações:

O projeto ainda está em uma fase inicial e pode apresentar bugs ou comportamentos inesperados.

Atualmente, os principais pontos que precisam de melhorias estão relacionados ao **tratamento de erros e à estabilidade da automação**, especialmente em situações como:

* indisponibilidade ou instabilidade do site do INPI;
* falhas ou interrupções durante o download;
* alterações na estrutura do site;
* PDFs indisponíveis ou corrompidos;
* mudanças no formato ou conteúdo das publicações;
* arquivos já existentes no diretório de destino.
