import os

restaurantes = [{'nome':'praca', 'categoria':'japonesa', 'ativo':False},
                {'nome':'pizza sprema', 'categoria':'italiano', 'ativo':False},
                {'nome':'Cantina', 'categoria':'italiano', 'ativo':True}]


def exibir_nome_do_programa():
    print("""
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    """)

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar restaurante")
    print("3. Alterar estado do restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system("cls")
    print("Encerrando programa\n")

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print("Opcao invalida")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto) + 4)
    print(linha)
    print(f'* {texto} *')
    print(linha)

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f'Digite o nome da categoria do Restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"O Restaurante {nome_do_restaurante} cadastrado com sucesso!")

    voltar_ao_menu_principal()

def altenar_estado_restaurante():
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Nao encontrado')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    for x in restaurantes:
        print(f" - O restaurante {x['nome']} é da Catagoria: {x['categoria']} e esta { 'ativado' if x['ativo'] else 'desativado' } ")
    voltar_ao_menu_principal()
    
def escolher_opcao():
    opcao_escolhida = int(input('Escolhar uma opção: '))
    print(f'Você escolheu a opção {opcao_escolhida}')
    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        altenar_estado_restaurante()
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()