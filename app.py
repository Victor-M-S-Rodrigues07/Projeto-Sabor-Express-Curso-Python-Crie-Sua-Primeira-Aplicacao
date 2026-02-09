import os

lista_de_restaurantes = ["Mc Donalds", "Pizza Hut", "Casa do Pastel"]

def exibir_nome_do_programa():

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

    print ("1 - Cadastrar restaurante")
    print ("2 - Listar restaurantes")
    print ("3 - Ativar restaurante")
    print ("4 - Sair\n")

def escolher_opcao():

    try:

        opcao_escolhida = int(input ("Escolha uma opção: "))
        if opcao_escolhida == 1:

            cadastrar_restaurante()

        elif opcao_escolhida == 2:

            listar_restaurantes()

        elif opcao_escolhida == 3:

            print ("Ativar restaurante")

        elif opcao_escolhida == 4:

            encerrar_app()

        else:

            opcao_invalida()

    except:

        opcao_invalida()

def retornar_ao_menu():

    input ("\nDigite uma tecla para voltar ao menu: ")
    main()

def exibir_subtitulos (subtitulo):

    os.system ("cls")
    print (f"{subtitulo}\n")

def cadastrar_restaurante():

    exibir_subtitulos ("Cadastro de Restaurantes")
    nome_do_restaurante = input ("Digite o nome do restaurante a ser cadastrado: ")
    lista_de_restaurantes.append (nome_do_restaurante)

    print (f"Restaurante {nome_do_restaurante} cadastrado com sucesso!")
    retornar_ao_menu()

def listar_restaurantes():

    exibir_subtitulos ("Listando os restaurantes...")

    for restaurante_indice in lista_de_restaurantes:

        print (f"*  {restaurante_indice}")
    
    retornar_ao_menu()

def encerrar_app ():

    exibir_subtitulos ("Encerrando o programa...")

def opcao_invalida():

    input ("Opção Inválida. Aperte qualquer tecla para voltar ao menu principal: ")
    main()

def main():

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