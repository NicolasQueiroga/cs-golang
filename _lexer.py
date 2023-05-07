from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lg = LexerGenerator()

    def _add_tokens(self):
        self.lg.add("PROGRAM", r"Let\'s\s+get\s+this\s+done")
        self.lg.add("VARIABLES_DECLARATION", r"variables")
        self.lg.add("FUNCITONS_DECLARATION", r"functions")
        self.lg.add("LOOP", r"match")
        self.lg.add("END_LOOP", r"end\s+match")
        self.lg.add("ROUND", r"round")
        self.lg.add("END_ROUND", r"ended")
        self.lg.add("BUY", r"buy")
        self.lg.add("KILL", r"kill")
        self.lg.add("DEATH", r"death")
        self.lg.add("PLANT", r"plant")
        self.lg.add("DEFUSE", r"defuse")
        self.lg.add("IF", r"if")
        self.lg.add("ELSE", r"else")
        self.lg.add("EXECUTE", r"execute")
        self.lg.add("GG", r"GG\s+WP")
        self.lg.add("ALIVE", r"alive")
        self.lg.add("SCORE", r"score")

        # Operadores
        self.lg.add("EQ", r"==")
        self.lg.add("NEQ", r"!=")
        self.lg.add("GT", r">")
        self.lg.add("GTE", r">=")
        self.lg.add("LT", r"<")
        self.lg.add("LTE", r"<=")
        self.lg.add("AND", r"&&")
        self.lg.add("OR", r"\|\|")

        # Palavras reservadas
        self.lg.add("KNOWN_AS", r"known\s+as")
        self.lg.add("HAVE_BEEN_DECLARED", r"have\s+been\s+declared")
        self.lg.add("PRINT_INVENTORY", r"printInventory")
        self.lg.add("RELOAD", r"reload")
        self.lg.add("FOR", r"for")
        self.lg.add("FROM", r"from")
        self.lg.add("POSITION", r"default|safe|open|hidden")
        self.lg.add("AT", r"at")
        self.lg.add("SECONDS_REMAINING", r"seconds\s+remaining")
        self.lg.add("WITH", r"with")

        # Identificadores
        self.lg.add("DATA_TYPE", r"(weapon|playerID|team|bombSiteID)")
        self.lg.add("TEAM_IDENTIFIER", r"(T|CT)")
        self.lg.add(
            "WEAPON_IDENTIFIER",
            r"(AK-47|M4A4|M4A1-S|AWP|SG\s+553|Glock-18|USP-S|P2000|Desert\s+Eagle|Tec-9|Five-SeveN|MP7|MP9|PP-Bizon|MAC-10|Galil\s+AR|FAMAS|Sawed-Off|Nova|XM1014|MAG-7|M249|Negev)",
        )
        self.lg.add("BOMB_SITE", r"(A|B)")
        self.lg.add(
            "ROUND_END",
            r"round\s+ended\s+with\s+(T|CT)\s+as\s+(Terrorists|Counter-Terrorists)\s+\(\d+-\d+\)",
        )
        self.lg.add("ROUND_WINNER", r"(Terrorists|Counter-Terrorists|Draw)")

        # Outros tokens
        self.lg.add("NEWLINE", r"\n")
        self.lg.add("COLON", r":")
        self.lg.add("MINUS", r"\-")
        self.lg.add("COMMA", r",")
        self.lg.add("DOT", r"\.")
        self.lg.add("LPAREN", r"\(")
        self.lg.add("RPAREN", r"\)")
        self.lg.add("LBRACE", r"{")
        self.lg.add("RBRACE", r"}")
        self.lg.add("SECONDS", r"seconds")

        # All
        self.lg.add("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*")

        # Literais
        self.lg.add("DIGIT", r"\d+")

        # Ignorar espaços em branco e quebras de linha
        # self.lg.ignore(r"[ \t]+")
        self.lg.ignore(r"\s")

    def get_lexer(self):
        self._add_tokens()
        return self.lg.build()
