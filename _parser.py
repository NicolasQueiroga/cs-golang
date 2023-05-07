import rply

from rply import ParserGenerator
from _lexer import Lexer


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names, accepted by the parser.
            [
                "PROGRAM",
                "VARIABLES_DECLARATION",
                "FUNCITONS_DECLARATION",
                "LOOP",
                "END_LOOP",
                "ROUND",
                "END_ROUND",
                "BUY",
                "ALIVE",
                "SCORE",
                "KILL",
                "DEATH",
                "PLANT",
                "DEFUSE",
                "IF",
                "ELSE",
                "EXECUTE",
                "DOT",
                "GG",
                "EQ",
                "NEQ",
                "GT",
                "GTE",
                "LT",
                "LTE",
                "AND",
                "OR",
                "KNOWN_AS",
                "HAVE_BEEN_DECLARED",
                "PRINT_INVENTORY",
                "RELOAD",
                "FOR",
                "FROM",
                "POSITION",
                "AT",
                "SECONDS_REMAINING",
                "WITH",
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
                "SECONDS",
                "IDENTIFIER",
                "DIGIT",
            ]
        )

    def parse(self):
        @self.pg.production("program : PROGRAM variables_declaration functions_declaration game_loop GG")
        @self.pg.production("program : PROGRAM variables_declaration game_loop GG")
        @self.pg.production("program : PROGRAM GG")
        def program(p):
            return p
        
        @self.pg.production("variables_declaration : VARIABLES_DECLARATION LBRACE variables RBRACE")
        def variables_declaration(p):
            return p
        
        @self.pg.production("variables : DATA_TYPE COLON IDENTIFIER KNOWN_AS IDENTIFIER COMMA variables")
        @self.pg.production("variables : DATA_TYPE COLON IDENTIFIER KNOWN_AS IDENTIFIER")
        @self.pg.production("variables : DATA_TYPE COLON TEAM_IDENTIFIER KNOWN_AS IDENTIFIER COMMA variables")
        @self.pg.production("variables : DATA_TYPE COLON TEAM_IDENTIFIER KNOWN_AS IDENTIFIER")
        @self.pg.production("variables : DATA_TYPE COLON WEAPON_IDENTIFIER KNOWN_AS IDENTIFIER COMMA variables")
        @self.pg.production("variables : DATA_TYPE COLON WEAPON_IDENTIFIER KNOWN_AS IDENTIFIER")
        @self.pg.production("variables : DATA_TYPE COLON BOMB_SITE KNOWN_AS IDENTIFIER COMMA variables")
        @self.pg.production("variables : DATA_TYPE COLON BOMB_SITE KNOWN_AS IDENTIFIER")
        def variables(p):
            return p
        
        @self.pg.production("functions_declaration : FUNCITONS_DECLARATION LBRACE functions RBRACE")
        def functions_declaration(p):
            return p
        
        @self.pg.production("functions : IDENTIFIER LPAREN identifiers RPAREN LBRACE round_statements RBRACE COMMA functions")
        @self.pg.production("functions : IDENTIFIER LPAREN identifiers RPAREN LBRACE round_statements RBRACE")
        def functions(p):
            return p
        
        @self.pg.production("identifiers : IDENTIFIER COMMA identifiers")
        @self.pg.production("identifiers : IDENTIFIER")
        def identifiers(p):
            return p
        
        @self.pg.production("game_loop : LOOP DIGIT COLON DIGIT LBRACE loop RBRACE")
        def game_loop(p):
            return p
        
        @self.pg.production("loop : ROUND boolean_expression LBRACE round_statements RBRACE")
        def loop(p):
            return p
        
        @self.pg.production("boolean_expression : IDENTIFIER EQ IDENTIFIER")
        @self.pg.production("boolean_expression : IDENTIFIER NEQ IDENTIFIER")
        @self.pg.production("boolean_expression : IDENTIFIER GT IDENTIFIER")
        @self.pg.production("boolean_expression : IDENTIFIER GTE IDENTIFIER")
        @self.pg.production("boolean_expression : IDENTIFIER DOT ALIVE AND boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT ALIVE OR boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT SCORE AND boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT SCORE OR boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT SCORE GT boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT SCORE GTE boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT SCORE LT boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT SCORE LTE boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT SCORE EQ boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT SCORE NEQ boolean_expression")
        @self.pg.production("boolean_expression : IDENTIFIER DOT SCORE")
        @self.pg.production("boolean_expression : IDENTIFIER DOT ALIVE")
        def boolean_expression(p):
            return p
        
        @self.pg.production("round_statements : round_statement COMMA round_statements")
        @self.pg.production("round_statements : round_statement")
        def round_statements(p):
            return p
        
        @self.pg.production("round_statement : IF boolean_expression LBRACE round_statements RBRACE COMMA ELSE LBRACE round_statements RBRACE COMMA round_statements")
        @self.pg.production("round_statement : IF boolean_expression LBRACE round_statements RBRACE COMMA ELSE LBRACE round_statements RBRACE")
        @self.pg.production("round_statement : IF boolean_expression LBRACE round_statements RBRACE COMMA round_statements")
        @self.pg.production("round_statement : IF boolean_expression LBRACE round_statements RBRACE")
        @self.pg.production("round_statement : EXECUTE IDENTIFIER LPAREN identifiers RPAREN")
        @self.pg.production("round_statement : BUY IDENTIFIER FOR DIGIT")
        @self.pg.production("round_statement : KILL IDENTIFIER FROM IDENTIFIER")
        @self.pg.production("round_statement : DEATH IDENTIFIER FROM IDENTIFIER")
        @self.pg.production("round_statement : PLANT POSITION IDENTIFIER AT IDENTIFIER")
        @self.pg.production("round_statement : DEFUSE IDENTIFIER AT BOMB_SITE WITH DIGIT SECONDS_REMAINING")
        def round_statement(p):
            return p
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)
        
    def get_parser(self):
        return self.pg.build()