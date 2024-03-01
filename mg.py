import os

codigos = []


def exibir_titulo():  # Exibe o titulo do programa.
    print('''
 █▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀█   █▀▀█ █▀▀▀█ █▀▀▄ ▀█▀ █▀▀█ █▀▀▀█
 █░░░ █▄▄█ █░▒█ █▄▄█ ▀▀▀▄▄ ░▒█░░ █▄▄▀ █▄▄█ █▄▄▀   █░░░ █░░▒█ █░▒█ ░█░ █░▄▄ █░░▒█
 █▄▄█ █░▒█ █▄▄▀ █░▒█ █▄▄▄█ ░▒█░░ █░▒█ █░▒█ █░▒█   █▄▄█ █▄▄▄█ █▄▄▀ ▄█▄ █▄▄█ █▄▄▄█
''')


def opcoes():  # Exibe as opções do programa disponivel.
    print("Digite 1- para cadastar um novo Codigo.")
    print("Digite 2- para ver os codigos cadastrados.")
    print("Digite 3- para Sair.\n")


def voltar_ao_menu_principal():  # Solicita uma tecla para voltar ao menu principal.
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()


def lista_de_codigos():  # Exibe a lista de codigos digitados pelo usuário.
    os.system("cls")
    print("𝚂𝚎𝚞𝚜 𝚌𝚘𝚍𝚒𝚐𝚘𝚜 𝚌𝚊𝚍𝚊𝚜𝚝𝚛𝚊𝚍𝚘𝚜 𝚜𝚊̃𝚘.n")
    for codigo in codigos:
        nome_codigo = codigo
        print(f"- {nome_codigo}")

    voltar_ao_menu_principal()


def cadastar_um_codigo():  # Essa função é responsavel por um codigo do usuário.
    os.system("cls")
    print("𝙲𝚊𝚍𝚊𝚜𝚝𝚊𝚛 𝚞𝚖 𝙲𝚘𝚍𝚒𝚐𝚘.\n")
    novo_codigo = input("Digite o codigo: ")
    dados_do_codigo = {novo_codigo}
    codigos.append(dados_do_codigo)
    print(f"O codigo {novo_codigo} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()


def finalizar_execucao():  # Limpa e exibe uma mensagem termino do programa.
    os.system("cls")
    print("Execução encerrada!!")


def opcao_invalida():  # Exibe uma mensagem de opção invalida e retorna ao menu principal.
    print("opção invalida!!")
    voltar_ao_menu_principal()


def escolher_opcao():  # Solicita e executa uma opção escolhida pelo usuário.

    try:
        opcao = int(input("Digite sua escolha: "))

        if opcao == 1:
            cadastar_um_codigo()

        elif opcao == 2:
            lista_de_codigos()

        elif opcao == 3:
            finalizar_execucao()

        else:
            opcao_invalida()

    except:
        opcao_invalida()


def main():  # Função principal que inicia o programa.
    os.system("cls")
    exibir_titulo()
    opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
