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

Regras
- A palavra secreta é escolhida de forma aleatória de entre um conjunto pré-determinado de palavras;
- As letras da palavra secreta são exibidas como traços
- O jogador deve sugerir apenas uma letra de a-z por ronda, não sendo aceite mais do que uma letra por ronda ou qualquer outro caracter
- O jogador poderá cometer até 6 erros, após cometer 6 erros perdeu o jogo.
- Um erro é apenas quando o jogador sugere uma letra que não consta da palavra secreta, não constituindo um erro a introdução de caracteres que não sejam letras nem de letras repetidas

Execução
 - Ter Python 3
 - Fazer o download dos ficheiros main.py e jogo.py
 - Executar o programa

Exemplo de utilização



Bem vindo(a) ao jogo da forca

Regras:

-Cada traço representa uma letra da palavra secreta
-Em cada tentiva deverá indicar uma letra
-O número máximo de tentativas erradas é igual a 6
-Vitória: Descobrir a palavra secreta antes de atingir o nº máximo de erros
-Derrota: Atingir o nº máximo de erros (6) antes de descobrir a palavra secreta
Queres jogar? (Escreva jogar para o jogo iniciar ou sair para abandonar o jogo): jogar
 _   _   _   _   _   _   _ 
Introduza uma letra:e
['e']
Letra errada
 _   _   _   _   _   _   _ 
Introduza uma letra:o
['e', 'o']
Letra errada
 _   _   _   _   _   _   _ 
Introduza uma letra:a
['e', 'o', 'a']
 _  a  _   _  a  _  a
Introduza uma letra:g
['e', 'o', 'a', 'g']
g a  _   _  a  _  a
Introduza uma letra:r
['e', 'o', 'a', 'g', 'r']
g a r r a  _  a
Introduza uma letra:f
['e', 'o', 'a', 'g', 'r', 'f']
Vitória!! A palavra era: garrafa
Queres jogar novamente? (Escreva jogar para o jogo novamente ou sair para abandonar o jogo): 