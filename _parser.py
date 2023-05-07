from rply import ParserGenerator, Token
from _ast import *


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            [
                "PROGRAM",
                "BLOCK",
                "FOR",
                "FROM",
                "POSITION",
                "VARIABLES_DECLARATION",
                "LOOP",
                "SECONDS_REMAINING",
                "WITH",
                "END_LOOP",
                "ROUND",
                "END_ROUND",
                "BUY",
                "KILL",
                "BOMB",
                "AT",
                "DEATH",
                "PLANT",
                "DEFUSE",
                "THEN",
                "ELSE",
                "EXECUTE",
                "GG",
                "EQ",
                "NEQ",
                "GT",
                "GTE",
                "LT",
                "LTE",
                "KNOWN_AS",
                "HAVE_BEEN_DECLARED",
                "PRINT_INVENTORY",
                "RELOAD",
                "DATA_TYPE",
                "TEAM_IDENTIFIER",
                "WEAPON_IDENTIFIER",
                "BOMB_SITE",
                "ROUND_END",
                "ROUND_WINNER",
                "NEWLINE",
                "COLON",
                "MINUS",
                "COMMA",
                "DOT",
                "LPAREN",
                "RPAREN",
                "LBRACE",
                "RBRACE",
                "HEADSHOT",
                "DEFAULT",
                "SAFE",
                "OPEN",
                "HIDDEN",
                "SECONDS",
                "IDENTIFIER",
                "DIGIT",
            ],
            precedence=[
                ("left", ["THEN", "ELSE", "EXECUTE"]),
                ("left", ["AND", "OR"]),
                ("left", ["EQ", "NEQ", "GT", "GTE", "LT", "LTE"]),
            ],
        )
        self.variables = {}
    
    def parse(self):
        self._add_rules()
        return self.pg.build()
    
    def _add_rules(self):
        @self.pg.production('program : PROGRAM VARIABLES_DECLARATION BLOCK GG')
        def program(p):
            return ProgramNode(p[1], p[2])
        
        @self.pg.production('variables_declaration : VARIABLES_DECLARATION BLOCK HAVE_BEEN_DECLARED')
        def variables_declaration(p):
            return VariablesDeclarationNode(p[1])
        
        @self.pg.production('variable_declaration : DATA_TYPE COLON IDENTIFIER KNOWN_AS IDENTIFIER COMMA')
        def variable_declaration(p):
            # add variable to variables dictionary
            self.variables[p[4].value] = p[2].value
            return VariableNode(p[0], p[2], p[4])
        
        @self.pg.production('game_loop : LOOP DIGIT COLON DIGIT BLOCK END_LOOP')
        def game_loop(p):
            return GameLoopNode(p[1], p[3], p[4])
        
        @self.pg.production('loop : ROUND BLOCK COMMA BLOCK END_ROUND')
        def loop(p):
            return LoopNode(p[1], p[3])
        
        # statements can have multiple statements
        @self.pg.production('statements : statement statements')
        @self.pg.production('statements : statement')
        def statements(p):
            return StatementsNode(p)
        
        @self.pg.production('statement : BUY WEAPON_IDENTIFIER FOR DIGIT')
        def buy(p):
            return WeaponBuyNode(p[1], p[3])
        
        @self.pg.production('statement : KILL IDENTIFIER FROM WEAPON_IDENTIFIER')
        def kill(p):
            return KillNode(p[1], p[3])
        
        @self.pg.production('statement : DEATH IDENTIFIER FROM WEAPON_IDENTIFIER')
        def death(p):
            return DeathNode(p[1], p[3])
        
        @self.pg.production('statement : PLANT POSITION BOMB AT BOMB_SITE')
        def plant(p):
            return BombPlantNode(p[1], p[4])
        
        @self.pg.production('statement : DEFUSE BOMB AT BOMB_SITE WITH DIGIT SECONDS_REMAINING')
        def defuse(p):
            return BombDefuseNode(p[4], p[6])

        # @self.pg.production('round_end : ROUND ENDED WITH TEAM_IDENTIFIER AS ROUND_WINNER LPAREN DIGIT MINUS DIGIT RPAREN')
        # def round_end(p):
        #     return RoundEndNode(p[3], p[5], p[7], p[9])
        
