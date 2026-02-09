# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_nomes = ["João Paulo II", "Ana Rosa", "Maria Antonieta"]
# lista_anos = [2005, 2026]

# print (lista_numeros)
# print (lista_nomes)
# print (lista_anos)



# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# lista_linha_1_azul = ["Tucuruvi", "Parada Inglesa", "Jardim São Paulo - Ayrton Senna", "Santana", "Carandiru", "Portuguesa - Tietê", "Armênia", "Tiradentes", "Luz", "São Bento", "Sé", "Japão - Liberdade", "São Joaquim", "Vergueiro - Sebrae", "Paraíso", "Ana Rosa", "Vila Mariana", "Santa Cruz", "Praça da Árvore", "Saúde - Ultrafarma", "São Judas", "Conceição", "Jabaquara - Comitê Paralímpico Brasileiro"]

# for estacao in lista_linha_1_azul:

#     print (estacao)



# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# soma_numeros_impares = 0

# for indice in range (1, 11, 2):

#     soma_numeros_impares = soma_numeros_impares + indice

# print (soma_numeros_impares)



# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# for indice in range (10, 0, -1):

#     print (indice)


# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# numero_usuario = int (input ("Digite um número para criar a tabuada: "))

# for indice in range (1, 11, 1):

#     produto = numero_usuario * indice

#     print (f"{numero_usuario} * {indice} = {produto}")



# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# lista_numeros = [10, 50, 3, 67, 25, 38, 98, 24, -89, "oi", 50]
# soma = 0

# try:
    
#     for indice in lista_numeros:

#         soma = soma + indice

#     print (soma)

# except Exception as e:

#     print (f"Erro, a lista contém o elemento: '{indice}' que não é um número! Corrija")



# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

# lista_numeros = [10, 9.45, 9.3, 9.5, 8.9, 9, "95"]
# soma = 0
# contador = 0

# try:

#     for indice in lista_numeros:

#         contador = contador + 1
#         soma = (soma + indice)

#     media = soma / contador
#     print (media)

# except ZeroDivisionError:

#     print (f"A lista está vazia! Tente de novo")
    
# except Exception as e:

#     print (f"O elemento {e} não é um número")

