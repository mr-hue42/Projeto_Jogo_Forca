palavras = ["Mesa","Cadeira","Livro","Copo","Mochila","Garrafa","Teclado",
            "Espelho", "Candeeiro","Tesoura"]
import random

palavra_selecionada = random.choice(palavras).lower()

letras = [" _ "] * len(palavra_selecionada)

print(palavra_selecionada)
print(letras)
