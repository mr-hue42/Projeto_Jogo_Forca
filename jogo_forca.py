print("Bem vindo(a) ao jogo da forca")
print()
print("Regras:")
print()
print("-Cada traço representa uma letra da palavra secreta")
print("-Em cada tentiva deverá indicar uma letra")
print("-O número máximo de tentativas erradas é igual a 6")
print("-Vitória: Descobrir a palavra secreta antes de atingir o nº máximo de erros")
print("-Derrota: Atingir o nº máximo de erros (6) antes de descobrir a palavra secreta")

import random

palavras = ["Mesa","Cadeira","Livro","Copo","Mochila","Garrafa","Teclado",
            "Espelho", "Candeeiro","Tesoura"]

palavra_selecionada = random.choice(palavras).lower()

letras = [" _ "] * len(palavra_selecionada)

while " _ " in letras:
    print(" ".join(letras))
    
    letra=input("Introduza uma letra:")
    
    if letra in palavra_selecionada:
        for i in range(len(palavra_selecionada)):
            if palavra_selecionada[i]==letra:
                letras[i] = letra
                
    else:
        print("Erro")
print(f"Vitória!! A palavra era: {palavra_selecionada}")

