#1. Lista de números ao quadrado:
# numeros = list(range(1,11))
# for numero in numeros:  
#     print(numero**2)

#2. Modificar lista de linguagens:
# linguagens = ["Python", "Java", "C++", "JavaScript"]
# linguagens.remove("C++")
# linguagens.append("Ruby")
# print(linguagens)

#3. Informações de um livro
# livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}")

#4. Contar ocorrências de caracteres
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))