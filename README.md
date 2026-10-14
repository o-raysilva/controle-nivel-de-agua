# 💧 Programa Teste para Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge) ![Projeto](https://img.shields.io/badge/Projeto-Controle%20de%20Níveis%20de%20Água-00AEEF?style=for-the-badge)

Programa teste desenvolvido em Python para **simular o nível de água de um reservatório** e exibir no terminal a situação correspondente, destacada com uma cor específica por meio da biblioteca **Colorama**.<br>

O nível é definido aleatoriamente a cada execução, sem necessidade de informar dados. O programa não realiza medições reais do reservatório.<br>

Ao executar, o terminal apresenta:
* Nível atual do reservatório, de 1 a 5
* Situação correspondente ao nível
* Mensagem destacada com a cor definida para a situação

## 🌊 Níveis do Reservatório

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## ⚙️ Funcionamento

* As situações e as respectivas cores são armazenadas em uma **lista aninhada**.
* A função `randint(0, 4)` sorteia o índice de um dos cinco níveis.
* A função `exibir_situacao()` identifica a mensagem e a cor correspondentes ao nível sorteado e apresenta o resultado no terminal.
* Após a mensagem, `Style.RESET_ALL` restaura o estilo padrão do terminal.

## 🧪 Testes de Execução

### Nível 1 - Muito baixo (crítico)
![Nível 1 - Vermelho](imagens/nivel_1.png)

### Nível 2 - Baixo
![Nível 2 - Amarelo](imagens/nivel_2.png)

### Nível 3 - Médio
![Nível 3 - Verde](imagens/nivel_3.png)

### Nível 4 - Alto
![Nível 4 - Ciano](imagens/nivel_4.png)

### Nível 5 - Muito alto (alerta)
![Nível 5 - Azul](imagens/nivel_5.png)
  
## ▶ Como executar

* Certifique-se de ter o **Python** instalado no computador.
* Instale a biblioteca Colorama pelo terminal, caso ainda não esteja instalada:

  ```bash
  pip install colorama
  ```

* Abra a pasta do projeto em um terminal.
* Execute o arquivo `app.py` utilizando o comando:

  ```bash
  python app.py
  ```

* O programa exibirá um nível aleatório e sua situação correspondente. Execute-o novamente para realizar outra simulação.
