# CS:GO lang

---

Made by: Nicolas Maciel Queiroga

---

## To-Do List

- [x]  Estruturar a linguagem segundo o padrão ********EBNF********
- [ ]  Utilizar as ferramentas Flex e Bison (ou semelhantes) para realizar as etapas de Análise Léxica e Sintática
- [ ]  Utilizar a LLVM (ou semelhantes - incluindo o próprio compilador) para implementar a sua linguagem até a fase final de compilação. Não é preciso implementar um compilador novo
- [ ]  Criar um exemplo de testes que demonstre as características da sua Linguagem
- [ ]  Montar uma apresentação com slides apresentando sua linguagem (Motivação, Características, Curiosidades e Exemplos)
- [ ]  Colocar no Github

# EBNF

```bash
PROGRAM = "Let's get this done", VARIABLES_DECLARATION, GAME_LOOP, "GG WP";

GAME_LOOP = "match", DIGIT, ":", DIGIT, { LOOP }, "end match";

LOOP = "round", DIGIT, ":", DIGIT, ":", ROUND_OUTCOME, { ROUND_STATEMENT };

ROUND_STATEMENT = ( WEAPON_BUY | KILL | DEATH | BOMB_PLANT | BOMB_DEFUSE | ROUND_END );

VARIABLES_DECLARATION = "variables", { VARIABLES }, "have been declared";

VARIABLES = DATA_TYPE, ":", IDENTIFIER, "known as", IDENTIFIER;

WEAPON_BUY = "buy", WEAPON_IDENTIFIER, "for", DIGIT;

KILL = "kill", IDENTIFIER, "with", WEAPON_IDENTIFIER, [ "headshot" ];

DEATH = "death", IDENTIFIER, "from", WEAPON_IDENTIFIER;

BOMB_PLANT = "plant", [ "default" | "safe" | "open" | "hidden" ], "bomb", "at", BOMB_SITE;

BOMB_DEFUSE = "defuse", [ "kit" ], "bomb", "at", BOMB_SITE, "with", DIGIT, "seconds remaining";

ROUND_END = "round", "ended", "with", TEAM_IDENTIFIER, "as", ROUND_WINNER, "(", DIGIT, "-", DIGIT, ")";

CONDITIONAL = "if", BOOLEAN_EXPRESSION, "then", BLOCK, [ "else", BLOCK ];

BLOCK = "{", { STATEMENT }, "}";

BOOLEAN_EXPRESSION = IDENTIFIER, ("==", | "!=", | ">", | "<", | ">=", | "<="), IDENTIFIER;

ARITHMETIC_EXPRESSION = EXPRESSION, ("+", | "-", | "*", | "/"), EXPRESSION;

FUNCTION = "execute", IDENTIFIER, "with", [ ARGUMENT, { ",", ARGUMENT } ];

ARGUMENT = IDENTIFIER | DIGIT | BOOLEAN;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

DATA_TYPE = ( "weapon" | "player" | "team" );

TEAM_IDENTIFIER = ( "T" | "CT" );

WEAPON_IDENTIFIER = ( "AK-47" | "M4A4" | "M4A1-S" | "AWP" | "SG 553" | "Glock-18" | "USP-S" | "P2000" | "Desert Eagle" | "Tec-9" | "Five-SeveN" | "MP7" | "MP9" | "PP-Bizon" | "MAC-10" | "Galil AR" | "FAMAS" | "Sawed-Off" | "Nova" | "XM1014" | "MAG-7" | "M249" | "Negev" );

BOMB_SITE = ( "A" | "B" );

ROUND_WINNER = ( "Terrorists" | "Counter-Terrorists" | "Draw" );

DIGIT = ( "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" );

LETTER = ( "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" | "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" );

ROUND_OUTCOME = ( "win" | "loss" | "draw" );
```

# Exemplos em código

## Jogo de simulação de Counter-Strike

```bash
Let's get this done
variables
  weapon:AK-47 known as gun1,
  weapon:M4A4 known as gun2,
  player:John known as player1,
  player:Sarah known as player2,
  team:T known as T,
  team:CT known as CT,
  bombSite:A known as siteA,
  bombSite:B known as siteB
have been declared
match 1:0
  round 1:0:win
    buy gun1 for 2700
    buy gun2 for 3100
    kill player1 with gun1
    kill player2 with gun2 headshot
    round ended with T as Terrorists (2-0)
  round 2:0:loss
    buy gun1 for 2700
    buy gun2 for 3100
    death player1 from gun1
    death player2 from gun2
    round ended with CT as Counter-Terrorists (0-2)
end match
GG WP
```

Neste exemplo, é definido um jogo de simulação de Counter-Strike. As variáveis declaradas são armas (AK-47 e M4A4), jogadores (John e Sarah), times (Terroristas e Contra-Terroristas) e locais de plantação de bomba (A e B). O jogo tem duas rodadas, em que as ações são registradas para cada uma das rodadas. Na primeira rodada, os Terroristas (T) vencem a rodada ao matar os dois jogadores adversários. Na segunda rodada, os Contra-Terroristas (CT) vencem a rodada ao matar os dois jogadores Terroristas.

## Programa de avaliação de desempenho de jogadores

```bash
Let's get this done
variables
  player:Tom known as player1,
  player:Bob known as player2,
  player:Sue known as player3,
  player:Jen known as player4
have been declared
if player1.score > player2.score then
{
  execute printScore(player1)
  execute printScore(player2)
}
else
{
  execute printScore(player2)
  execute printScore(player1)
}
if player3.kills > player4.kills then
{
  execute printKills(player3)
  execute printKills(player4)
}
else
{
  execute printKills(player4)
  execute printKills(player3)
}
```

Neste exemplo, é definido um programa que avalia o desempenho de quatro jogadores (Tom, Bob, Sue e Jen). As variáveis declaradas são os quatro jogadores. O programa verifica o score de cada um dos dois primeiros jogadores e imprime o score do jogador com o score mais alto primeiro. Em seguida, verifica o número de kills de cada um dos dois últimos jogadores e imprime o número de kills do jogador com o número mais alto primeiro.

## Sistema de gerenciamento de armas de fogo

```bash
Let's get this done
variables
  player:John known as player1,
  weapon:AK-47 known as gun1,
  weapon:M4A4 known as gun2,
  weapon:AWP known as gun3
have been declared

execute printInventory()

if gun1.ammo < 30 then
{
  execute reload(gun1)
}
if gun2.ammo < 30 then
{
  execute reload(gun2)
}
if gun3.ammo < 5 then
{
  execute reload(gun3)
}
```

Neste exemplo, além das declarações das variáveis **`player1`** e armas **`gun1`**, **`gun2`** e **`gun3`**, há a chamada da função **`printInventory()`**, que deve imprimir na tela as informações sobre o inventário do jogador.

Por fim, há uma verificação do nível de munição de cada uma das armas. Caso alguma delas esteja abaixo do valor mínimo (30 balas para **`gun1`** e **`gun2`**, e 5 balas para **`gun3`**), o código executa a função **`reload()`** para recarregar a arma.
