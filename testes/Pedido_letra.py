palavras = ["Mesa","Cadeira","Livro","Copo","Mochila","Garrafa","Teclado",
            "Espelho", "Candeeiro","Tesoura"]
import random

palavra_selecionada = random.choice(palavras).lower()

print(palavra_selecionada)

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


        

    
