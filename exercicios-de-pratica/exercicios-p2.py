# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

# numero_do_usuario = int(input ("Insira um número: "));

# if numero_do_usuario % 2 == 0:

#     print ("O número é par\n");

# else:

#     print ("O número é ímpar\n");

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

# idade = int (input ("Digite sua idade: "));

# if  0 <= idade <= 12:

#     print ("Você é uma Criança");

# elif 13 <= idade < 18:

#     print ("Você é um Adolescente");

# elif idade => 18:

#     print ("Você é Adulto");

# else:

#     print ("Digite uma idade válida");

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# nome_correto = "Fabiano";
# senha_correta = "7070704060";

# nome_usuario = input ("Digite o seu nome de usuário: ");
# senha_usuario = input ("Digite sua senha: ");

# if nome_usuario == nome_correto and senha_usuario == senha_correta:

#     print ("Bem vindo ao nosso site!!\n");

# else:

#     print ("Usuário ou senha incorreta. Tente novamente.\n");

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

# coordenada_x = int (input ("Digite a coordenada das abcissas (x): "));
# coordenada_y = int (input ("Digite a coordenada das ordenadas (y): "));

# if coordenada_x > 0 and coordenada_y > 0:

#     print (f"({coordenada_x},{coordenada_y}) - Primeiro Quadrante");

# elif coordenada_x < 0 and coordenada_y > 0:

#     print (f"({coordenada_x},{coordenada_y}) - Segundo Quadrante");

# elif coordenada_x < 0 and coordenada_y < 0:

#     print (f"({coordenada_x},{coordenada_y}) - Terceiro Quadrante");

# elif coordenada_x > 0 and coordenada_y < 0:

#     print (f"({coordenada_x},{coordenada_y}) - Quarto Quadrante");

# else:

#     print (f"({coordenada_x}, {coordenada_y}) - A coordenada está no eixo ou na origem (0,0)");