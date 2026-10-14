# Programa teste para controle de níveis de água
# Autor: o-raysilva

# Importação de bibliotecas:
from random import randint
from colorama import Fore, Style, just_fix_windows_console

# Inicialização:
just_fix_windows_console()
situacoes_cores = [ ["Muito baixo (crítico)", Fore.RED],
                 ["Baixo", Fore.YELLOW], 
                 ["Médio",Fore.GREEN],
                 ["Alto",Fore.CYAN],
                 ["Muito alto (alerta)",Fore.BLUE]
                   ]

# Função para exibição da situação com cor referente:
def exibir_situacao(nivel_atual, lista_base):
    print(
          "\n----Controle do nível da água----"
          f"\nNível atual: {nivel_atual+1}"
          f"\nSituação:{lista_base[nivel_atual][1]} {lista_base[nivel_atual][0]} {Style.RESET_ALL}"
          )

# Entrada utilizando número aleatório:
nivel = randint(0,4)

# Processamento com função:
exibir_situacao(nivel, situacoes_cores)

