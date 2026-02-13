# # 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# usuario = {"nome": "Zoe Anderson", "idade": 45, "cidade": "San Francisco - California"}

# print (usuario)

# # 2 - Utilizando o dicionário criado no item 1:

# # Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# # Adicione um campo de profissão para essa pessoa;
# # Remova um item do dicionário.

# usuario["idade"] = 35
# usuario["profissao"] = "Capitã da Polícia Militar"
# del usuario["cidade"]
# print (usuario)

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

# lista_quadrados = {x: x**2 for x in range (1, 6)}

# for indice in lista_quadrados:

#     print (indice)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# dicionario = {"linha": 1, "cor": "azul", "direcao": "norte-sul"}

# usuario_resposta = input ("Digite a chave a ser procurada no dicionário: ")



# if usuario_resposta in dicionario:

#     print ("Existe")

# else:

#      print ("Não existe")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

# frase = """No meio do caminho tinha uma pedra
# Tinha uma pedra no meio do caminho
# Tinha uma pedra
# No meio do caminho tinha uma pedra

# Nunca me esquecerei desse acontecimento
# Na vida de minhas retinas tão fatigadas
# Nunca me esquecerei que no meio do caminho
# Tinha uma pedra
# Tinha uma pedra no meio do caminho
# No meio do caminho tinha uma pedra"""

# contagem_palavras = {}
# palavras_divididas = frase.split()

# for palavra_indice in palavras_divididas:
#     contagem_palavras[palavra_indice] = contagem_palavras.get(palavra_indice, 0) + 1

# print(contagem_palavras)