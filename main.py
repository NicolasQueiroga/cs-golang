from _lexer import Lexer
from _parser import Parser


lexer = Lexer().get_lexer()
with open('test.gg', 'r') as f:
    text_input = f.read()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)

pg = Parser()
parser = pg.parse()
parser.parse(tokens).eval()