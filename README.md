# CS:GO lang

---

Made by: Nicolas Maciel Queiroga

---

## To-Do List

- [x]  Estruturar a linguagem segundo o padrão ********EBNF********
- [x]  Utilizar as ferramentas Flex e Bison (ou semelhantes) para realizar as etapas de Análise Léxica e Sintática
- [x]  Utilizar a LLVM (ou semelhantes - incluindo o próprio compilador) para implementar a sua linguagem até a fase final de compilação. Não é preciso implementar um compilador novo
- [x]  Criar um exemplo de testes que demonstre as características da sua Linguagem
- [x]  Montar uma apresentação com slides apresentando sua linguagem (Motivação, Características, Curiosidades e Exemplos)
- [x]  Colocar no Github

# EBNF

```bash
PROGRAM = "Lets_get_this_done", BLOCK, "GGWP";

LOOP = "round", BOOLEAN_EXPRESSION, { ROUND_STATEMENT };

ROUND_STATEMENT = ( FUNCTION_CALL | VARIABLES_DECLARATION | OPERATIONS );

VARIABLES_DECLARATION = IDENTIFIER, "::", DATA_TYPE, "known_as", IDENTIFIER;

FUNCTIONS_DECLARATION = "IDENTIFIER(ARGUMENTS) {ROUND_STATEMENTS};"

ARGUMENT = IDENTIFIER | DIGIT | BOOLEAN | ANY;

CONDITIONAL = "if", "(" BOOLEAN_EXPRESSION, ")", "{", BLOCK, "},", [ "else", "{", BLOCK, "}," ];

BLOCK = "{", { STATEMENT, "," }, "}";

BOOLEAN_EXPRESSION = IDENTIFIER, ("==", | "!=", | ">", | "<", | ">=", | "<="), IDENTIFIER;

ARITHMETIC_EXPRESSION = EXPRESSION, ("+", | "-", | "*", | "/"), EXPRESSION;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

DATA_TYPE = ( "weapon" | "playerID" | "team" | "bombSiteID" | "round" );

TEAM_IDENTIFIER = ( "T" | "CT" );

WEAPON_IDENTIFIER = ( "AK-47" | "M4A4" | "M4A1-S" | "AWP" | "SG 553" | "Glock-18" | "USP-S" | "P2000" | "Desert Eagle" | "Tec-9" | "Five-SeveN" | "MP7" | "MP9" | "PP-Bizon" | "MAC-10" | "Galil AR" | "FAMAS" | "Sawed-Off" | "Nova" | "XM1014" | "MAG-7" | "M249" | "Negev" );

BOMB_SITE = ( "A" | "B" );

ROUND_WINNER = ( "Terrorists" | "Counter-Terrorists" | "Draw" );

DIGIT | ROUND = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" );

LETTER = ( "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" );

ROUND_OUTCOME = ( "win" | "loss" | "draw" );
```

# Exemplos em código

## Jogo de simulação de Counter-Strike

```bash
Lets_get_this_done

gun1::weapon known_as "AK-47",
gun2::weapon known_as "AWP",
player1::playerID known_as "FalleN",
player2::playerID known_as "coldzera",
t1::team known_as "imp",
t2::team known_as "fur",
siteA::bombSiteID known_as "A",
siteB::bombSiteID known_as "B",
startRound::round known_as 1,
maxRound::round known_as 16,
cash::money known_as 800,

function printVar(var::weapon) {
  voip(var),
}

function buyGun(player::playerID, gun::weapon) {
  voip(player + " buys " + gun),
},

function execAstralis(site::bombSiteID, player::playerID) {
  voip("plant bomb at " + site + " and defend it with all players except " + player),
},

printVar(gun1),

  
currRound::round known_as startRound,
round_loop (currRound <= maxRound) {
  voip("Round " + currRound + " starts"),
  buyGun(player1, gun1),
  if (currRound == 2) {
    execAstralis(siteA, player2),
  }
  else {
    voip("Rush B, don't stop"),
  },
  currRound = currRound + 1,
},




GGWP
```

Esse código em CS:GOLang é uma representação simplificada de um script de jogo que descreve uma estratégia para um time em uma partida de Counter-Strike: Global Offensive (CSGO). Vou explicar linha por linha:

1. Declaração das variáveis:
   - gun1 é uma arma, especificamente uma AK-47.
   - gun2 é outra arma, uma AWP.
   - player1 é um jogador identificado como "FalleN".
   - player2 é outro jogador identificado como "coldzera".
   - t1 é uma equipe chamada "imp".
   - t2 é outra equipe chamada "fur".
   - siteA é um local de bomba identificado como "A".
   - siteB é outro local de bomba identificado como "B".
   - startRound é o número da rodada inicial, definido como 1.
   - maxRound é o número máximo de rodadas, definido como 16.
   - cash é o dinheiro inicial dos jogadores, definido como 800.

2. Declaração de uma função chamada "printVar" que recebe uma variável do tipo "weapon" (arma) e a imprime por meio de uma função chamada "voip".

3. Declaração de uma função chamada "buyGun" que recebe um jogador e uma arma como parâmetros. Essa função também usa a função "voip" para informar que o jogador comprou a arma.

4. Declaração de uma função chamada "execAstralis" que recebe um local de bomba e um jogador como parâmetros. Essa função usa a função "voip" para informar que o jogador deve plantar a bomba no local especificado e defender com todos os jogadores, exceto o jogador especificado.

5. Chamada da função "printVar" para imprimir a descrição da "gun1" (AK-47).

6. Início de um loop chamado "round_loop" que executa enquanto o número da rodada atual (currRound) for menor ou igual ao número máximo de rodadas (maxRound).

7. Dentro do loop, a função "voip" é usada para informar que a rodada atual está começando.

8. Em seguida, a função "buyGun" é chamada para o "player1" comprar a "gun1" (AK-47).

9. É feita uma verificação para saber se a rodada atual é a segunda (currRound == 2). Se for, a função "execAstralis" é chamada para o "player2" plantar a bomba no local "siteA" e defender.

10. Caso contrário, é usado a função "voip" para informar que o time deve fazer um rush no local "B" sem parar.

11. Incremento do número da rodada atual (currRound = currRound + 1).

12. Fim do loop "round_loop".

13. A mensagem "GGWP" é exibida, indicando "good game, well played" (bom jogo, bem jogado) como uma mensagem final.

Essa linguagem representa uma estratégia básica para um time no jogo CSGO, incluindo a compra de armas, plantio de bomba e ações específicas para rodadas específicas. É importante destacar que essa é apenas uma representação simplificada do jogo.


## Análises Léxica e Sintática

Para tokenizar o codigo de entrada, assim como realizar a análise sintática, foi utilizado a ferramenta `rply`

Para checar a análise sintática basta executar os seguintes comandos:

```bash
pip instal -r requirements.txt
python main.py
```

## Instruções Para Compilar o Compilador e Executar o Código Teste

- Para executar o projeto, é necessário ter o `cmake` instalado.
  - Para macOS, basta executar o seguinte comando:
  ```bash
  brew install cmake
  ```
  - Para Linux, basta executar o seguinte comando 
  ```bash
  sudo apt install cmake
  ```

- Dentro do diretorio do projeto `compilador`, basta seguir os seguintes passos:
```bash
mkdir build
cd build
cmake ..
make
```
  
- Para remover os feedbacks que tanto o comando `cmake` quanto o comando `make` geram, basta executa-los do seguinte jeito:
```bash
cmake .. > /dev/null
make > /dev/null
cd ..
./bin/main in/test.gg
```
