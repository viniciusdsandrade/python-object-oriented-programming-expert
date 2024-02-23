import os

restaurantes = []


def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)


def finalizar_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando o app')


def exibir_opcoes():
    print('1 - Cadastrar Restaurante')
    print('2 - Buscar Restaurante')
    print('3 - Listar Restaurantes')
    print('4 - Sair')


def cadastrar_novo_restaurante():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Cadastrar Restaurante')
    nome = input('Nome do restaurante: ')
    restaurantes.append(nome)
    print(f'Restaurante {nome} cadastrado com sucesso')
    input('Pressione enter para continuar')
    exibir_opcoes()
    escolher_opcao()


def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            print('Buscar restaurante')
        elif opcao == 3:
            listar_restaurantes()
        elif opcao == 4:
            print('Finalizar app')
            finalizar_app()
        else:
            print('Opção inválida')
            exibir_opcoes()
            escolher_opcao()
    except ValueError:
        print('Opção inválida')
        exibir_opcoes()
        escolher_opcao()


def listar_restaurantes():
    os.system('cls')
    print('Lista de Restaurantes:')
    if restaurantes:
        for i, restaurante in enumerate(restaurantes, 1):
            print(f'{i}. {restaurante}')
    else:
        print('Nenhum restaurante cadastrado ainda.')
    input('Pressione enter para continuar')
    exibir_opcoes()
    escolher_opcao()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
