palavras = ["Mesa","Cadeira","Livro","Copo","Mochila","Garrafa","Teclado",
            "Espelho", "Candeeiro","Tesoura"]
import random

jogar=input("Queres jogar? (Escreva jogar para o jogo iniciar ou sair para abandonar o jogo): ").lower()

while jogar == "jogar":

    palavra_selecionada = random.choice(palavras).lower()

    print(palavra_selecionada)

    letras = [" _ "] * len(palavra_selecionada)

    letras_usadas = [ ]

    erros = 0

    max_erros= 6

    while " _ " in letras and erros < max_erros:
        print(" ".join(letras))
    
        letra=input("Introduza uma letra:")
    
        if letra in letras_usadas:
            print("Letra já utilizada")
            continue
        letras_usadas.append(letra)
        print(letras_usadas)
    
        if letra in palavra_selecionada:
            for i in range(len(palavra_selecionada)):
                if palavra_selecionada[i]==letra:
                    letras[i] = letra
                
        else:
            print("Letra errada")
            erros += 1
    if " _ " not in letras:
        print(f"Vitória!! A palavra era: {palavra_selecionada}")
    else:
        print(f"Derrota!! A palavra era: {palavra_selecionada}")
    jogar= input("Queres jogar novamente? (Escreva jogar para continuar a jogar): ")

print("Obrigado por jogares")
