import os

lista_de_restaurantes = [{"nome": "Mc Donalds", "categoria": "Hamburguers", "estado": True},
                         {"nome": "Pizza Hut", "categoria": "Pizzas", "estado": False}, 
                         {"nome": "Casa do Pastel", "categoria": "Pastéis", "estado": False}]

def exibir_nome_do_programa():

    """Essa função tem por objetivo exibir o título do aplicativo (Sabor Express)"""

    print("""

██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░██████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░██████░░▄▀░░░░░░░░░░█░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░██████░░▄▀░░███████████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░██████░░▄▀░░░░░░░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░██████░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀▄▀▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░██████░░▄▀░░░░░░░░░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
█████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████████░░▄▀░░███████████░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████████████░░▄▀░░█████████░░▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░████░░▄▀░░░░░░░░░░█░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░█████████░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    """)

def exibir_opcoes():

    """Essa função exibe as opções disponíveis para o usuário escolher"""

    print ("1 - Cadastrar restaurante")
    print ("2 - Listar restaurantes")
    print ("3 - Alterar estado do restaurante")
    print ("4 - Sair\n")

def escolher_opcao():

    """Essa função é chamada para realizar a lógica de escolha quando o usuário digita uma opção.
    
    Input:
    - Opção escolhida pela usuário.
    """

    try:

        opcao_escolhida = int(input ("Escolha uma opção: "))
        if opcao_escolhida == 1:

            cadastrar_restaurante()

        elif opcao_escolhida == 2:

            listar_restaurantes()

        elif opcao_escolhida == 3:
            
            mudar_estado_restaurante()

        elif opcao_escolhida == 4:

            encerrar_app()

        else:

            opcao_invalida()

    except:

        opcao_invalida()

def retornar_ao_menu():

    """Função que retorna ao menu principal.
    
    Input:
    - Confirmação para voltar ao menu.
    """

    input ("\nDigite uma tecla para voltar ao menu: ")
    main()

def exibir_subtitulos (subtitulo):

    """Essa função exibe os subtítulos de cada função de forma decorada e com separações de linhas
    
    Input:
    - Subtítulo a ser exibido."""

    os.system ("cls")
    linha = "*" * len (subtitulo)

    print (linha)
    print (f"{subtitulo}")
    print (linha)
    print()

def cadastrar_restaurante():
    
    """ A função é responsável por cadastrar o restaurante inserido pelo usuário e adicionar os dados na lista de estabelecimentos.
    
    Input:
    - Nome do restaurante
    - Categoria
    
    Output:
    - Adiciona os dados para a lista de restaurantes
    """

    exibir_subtitulos ("Cadastro de Restaurantes")
    
    nome_do_restaurante = input ("Digite o nome do restaurante a ser cadastrado: ")
    categoria_restaurante = input ("Digite a categoria do restaurante: ")

    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria_restaurante, "estado": False}

    lista_de_restaurantes.append (dados_do_restaurante)

    print (f"Restaurante {nome_do_restaurante} cadastrado com sucesso!")
    retornar_ao_menu()

def listar_restaurantes():
    
    """Essa função exibe os restaurantes disponíveis na lista geral"""

    exibir_subtitulos ("Lista de Restaurantes")

    print (f"{"Nome do Restaurante".ljust(28)} | {"Categoria".ljust(25)} | {"Estado".ljust(25)}\n")

    for restaurante_indice in lista_de_restaurantes:

        nome_restaurante = restaurante_indice["nome"]
        categoria_restaurante = restaurante_indice["categoria"]
        status_restaurante = "Ativo" if restaurante_indice["estado"] else "Inativo"

        print (f"*  {nome_restaurante.ljust(25)} | {categoria_restaurante.ljust(25)} | {status_restaurante.ljust(25)}")
    
    retornar_ao_menu()

def mudar_estado_restaurante():
    
    """ A função altera o estado de um determinado restaurante, permitindo ativar, caso ele esteja desativado, e vice-versa.
    
    Input:
    - Nome do restaurante.
    
    Output:
    - Altera o estado do restaurante."""

    exibir_subtitulos ("Alterando restaurante do restaurante")

    nome_do_restaurante = input ("Digite o nome do restaurante: ")
    restaurante_encontrado = False

    for restaurante_indice in lista_de_restaurantes:

        if nome_do_restaurante == restaurante_indice["nome"]:

            restaurante_encontrado = True
            restaurante_indice["estado"] = not restaurante_indice["estado"]
            mensagem = f"O restaurante {nome_do_restaurante} foi ativado com sucesso!" if restaurante_indice["estado"] else f"O restaurante {nome_do_restaurante} foi desativado com sucesso!"

            print (mensagem)
    
    if not restaurante_encontrado:
        print ("Restaurante não foi encontrado!")

    retornar_ao_menu()

def encerrar_app():
    
    """Essa função informa o usuário e encerra o aplicativo."""

    exibir_subtitulos ("Encerrando o programa...")

def opcao_invalida():
    
    """ Função usada para caso o usuário digite uma opção que não está disponível
    
    Input:
    - Confirmação do usuário para retornar ao menu."""

    input ("Opção Inválida. Aperte qualquer tecla para voltar ao menu principal: ")
    main()

def main():
    
    """Função principal Main, responsável por iniciar o aplicativo, determinar o uso de outras funções dá outras providências"""

    os.system ("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == "__main__":
    main()

# Type() - define o tipo de dado do elemento;
# int() - transforma em inteiro {Semelhante ao ParseInt() do JavaScript};
# def - Define uma função {Function, no JavaScript};
# import - importa funcionalidades do Python;
# main() - função principal. Não pode ser importada;
# match - unidade de condicional, sendo uma opção ao "if" e "else".
# Try-Except: pede ao Python executar um código que, caso não funcione, acione outra função, o que não quebra o código.
# Tupla: lista que não pode ser alterada uma vez criada.
# Pass: pede para o programa ignorar uma função incompleta
# Dicionário: contém as informações em forma de listas dentre de uma lista, praticamente
# Regras de Negócio: definições constituídas pelo time para a criação do código
# Ternários: instruções simplificadas dentro de outras estruturas, como mensagens
# len(): função que entrega o tamanho dos elementos
# ljust(): justifica o conteúdo de uma string
# docstring: descrição adicionada a uma função