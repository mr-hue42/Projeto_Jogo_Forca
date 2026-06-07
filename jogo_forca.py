import random

def jogar_forca():#criar função para ser importada para ficheiro main
    print("Bem vindo(a) ao jogo da forca")
    print()
    print("Regras:")
    print()
    print("-Cada traço representa uma letra da palavra secreta")
    print("-Em cada tentiva deverá indicar uma letra")
    print("-O número máximo de tentativas erradas é igual a 6")
    print("-Vitória: Descobrir a palavra secreta antes de atingir o nº máximo de erros")
    print("-Derrota: Atingir o nº máximo de erros (6) antes de descobrir a palavra secreta")


#criar pool de palavras a selecionar para ser a palavra secreta
    palavras = ["Mesa","Cadeira","Livro","Copo","Mochila","Garrafa","Teclado",
                "Espelho", "Candeeiro","Tesoura"]
#controlar o inicio do jogo e inicio de novas rondas  
    while True:
       try:
           jogar=input("Queres jogar? (Escreva jogar para o jogo iniciar ou sair para abandonar o jogo): ").lower()
        
           if jogar not in ["jogar","sair"]:
                raise ValueError ("Resposta inválida")
           break
       except ValueError as erro:
                print(f'Erro:{erro}')
    
    if jogar== "sair":
        print("Obrigado. Volte sempre")
    
    while jogar == "jogar":

        palavra_selecionada = random.choice(palavras).lower()
    
        letras = [" _ "] * len(palavra_selecionada)
    
        letras_usadas = [ ]
#definição do nº de erros    
        erros = 0
    
        max_erros= 6
#analisar se as letras são repetidas, se estão na palavra  
        while " _ " in letras and erros < max_erros:
            print(" ".join(letras))
            while True:
                try:
                    letra=input("Introduza uma letra:")
                    if letra == "":
                        raise ValueError("Input vazio")
                    if len(letra) != 1:
                        raise ValueError("Mais de um caráter")
                    if not letra.isalpha():
                        raise ValueError("Não é uma letra")
                    break
                except ValueError as erro:
                    print(f"Erro: {erro}. Tenta novamente")
                
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
                erros += 1 #contagem de erros
        if " _ " not in letras:
            print(f"Vitória!! A palavra era: {palavra_selecionada}")
        else:
            print(f"Derrota!! A palavra era: {palavra_selecionada}")
        
        while True:
           try:
               jogar=input("Queres jogar novamente? (Escreva jogar para o jogo novamente ou sair para abandonar o jogo): ").lower()
            
               if jogar not in ["jogar","sair"]:
                    raise ValueError ("Resposta inválida")
               break
           except ValueError as erro:
                    print(f'Erro:{erro}')

        print("Obrigado por jogares")

