import os
import time
import logging

# Configura o logging para mostrar mensagens no terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para instalar qualquer software
def instalar_software(id_software, nome_software):
    try:
        logging.info(f'Instalando {nome_software}...')
        time.sleep(2)  # Espera 2 segundos (só pra simular, pode tirar depois)
        resultado = os.system(f'winget install --id {id_software} -e')
        if resultado == 0:
            logging.info(f'{nome_software} instalado com sucesso!')
        else:
            logging.error(f'Erro ao instalar {nome_software}.')
    except:
        logging.error(f'Algo deu errado ao instalar {nome_software}!')

# Lista de softwares com seus IDs e nomes
softwares = {
    0: ("Google.Chrome", "Google Chrome"),
    1: ("Microsoft.Office", "Microsoft Office"),
    2: ("XPDP273C0XHQH2", "Adobe PDF"),
    3: ("RARLab.WinRAR", "WinRAR"),
    4: ("VideoLAN.VLC", "VLC Media Player"),
    5: ("Zoom.Zoom", "Zoom"),
    6: ("Discord.Discord", "Discord")
}

# Função para mostrar o menu
def mostrar_menu():
    print("\n=== Menu de Instalação ===")
    print("0 - Instalar Google Chrome")
    print("1 - Instalar Pacote Office")
    print("2 - Instalar Adobe PDF")
    print("3 - Instalar WinRAR")
    print("4 - Instalar VLC Media Player")
    print("5 - Instalar Zoom")
    print("6 - Instalar Discord")
    print("7 - Sair")

# Função principal que roda o programa
def main():
    while True:
        mostrar_menu()
        try:
            escolha = int(input("Escolha uma opção: "))
            
            # Se escolher 7, sai do programa
            if escolha == 7:
                logging.info("Tchau! Programa encerrado.")
                break
            
            # Verifica se a opção existe no dicionário
            if escolha in softwares:
                id_software, nome_software = softwares[escolha]
                instalar_software(id_software, nome_software)
            else:
                logging.warning("Opção inválida! Escolha um número de 0 a 7.")
        
        except ValueError:
            logging.warning("Por favor, digite apenas números!")
        except KeyboardInterrupt:
            logging.info("\nVocê interrompeu o programa. Tchau!")
            break

# Inicia o programa
if __name__ == "__main__":
    main()
