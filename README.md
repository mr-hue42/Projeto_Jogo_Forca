# Projeto_Jogo_Forca

Objetivo geral: Criar um programa que permite ao utilizador jogar o jogo da forca

Objetivo do jogo: O utilizador deve adivinhar a palavra correta, indicando ao programa letras, consoante se as letras fazem parte ou não da palavra, será adicionado um parte do corpo do boneco, até as tentativas se esgotarem ou chegar-se à resposta correta.

Regras
- a palavra a deescobrir é apresentada em traços, em que cada traço corresponde a uma letra da palavra. P.e uma palavra que contenha 5 letras, como a palavra fruta será representada por 5 traços: _ _ _ _ _
- o jogador insere uma letra
- caso a letra esteja correta, a letra surge no lugar correto da palavra. P.e. o utilizador indica a letra a, será apresentado ao utilizador _ _ _ _ a.
- caso a letra esteja incorreta, os traços mantêm-se vazios.
- No jogo tradicional é desenhado um boneco (cabeça, tronco, braços e pernas) composto em 6 partes, por isso o utilizador terá um máximo de 6 erros.


Condições:
- Vitória - o utilizador insere as letras corretas antes de atingir o número máximo de erros (6)
- Derrota - o utilizador atinge o número máximo de erros (6) antes de descobrir todas as letras da palavra


Limitações
- Uma tentativa = uma letra
- Inputs = A a Z
- Máximo de 6 erros

Requisitos funcionais
- O programa deve selecionar aleatoriamente um palavra 
- O programa deve representar o nº de letras da palavra selecionada por traços;
- O programa permite ao utilizador inserir uma letra por tentativa
- O programa valida se a letra inserida faz parte da palavra selecionada
- O programa exibe o progresso da descoberta da palavra, exibindo os traços em falta para preencher e as letras selecionadas corretas nos sítio correto da palavra. As letras selecionadas de forma errada aparecem num canto abaixo.
- O programa deve exibir uma mensagem de final de jogo (Vitória ou Derrota)

Requisitos não funcionais:
- Validade input do utilizador. Aceitar a introdução de apenas letras (maisculas e minusculas de igual forma), ignorar números e caracteres especiais
- Compatível com o Python
- Apresentar mensagens simples e claras ao utilizador facilitando a compreensão do mesmo sobre a situação de jogo a cada momento.


Descrição

Programa do jogo desenvolvido em python, no qual o jogo exibe uma palavra secreta em traços e o jogador deverá descobrir a palavra sugerindo letras que possam fazer parte da palavra secreta.


