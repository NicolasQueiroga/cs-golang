from _lexer import Lexer
from _parser import Parser
from rply.errors import ParsingError



lexer = Lexer().get_lexer()
with open("test.gg", "r") as f:
    text_input = f.read()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()

def token_generator(token_list):
    for token in token_list:
        print(token)
        yield token

# Remova a parte que adiciona o token de final de arquivo ($end)
tokens = list(filter(lambda t: t.gettokentype() != '$end', tokens))

try:
    result = parser.parse(token_generator(tokens))
    print("Parsing successful!")
except Exception as e:
    print("Parsing failed:")
    print("Exception:", e)