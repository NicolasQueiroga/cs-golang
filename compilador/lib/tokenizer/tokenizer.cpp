#include <regex>
#include <iostream>
#include "tokenizer.hpp"

// #define DEBUG

Tokenizer::Tokenizer() : next("EOF", 0)
{
    this->reservedWords = std::make_shared<std::vector<std::string>>();
    this->reservedWords->push_back("Lets_get_this_done");
    this->reservedWords->push_back("variables");
    this->reservedWords->push_back("playerID");
    this->reservedWords->push_back("team");
    this->reservedWords->push_back("bombSiteID");
    this->reservedWords->push_back("weapon");
    this->reservedWords->push_back("function");
    this->reservedWords->push_back("match");
    this->reservedWords->push_back("round");
    this->reservedWords->push_back("if");
    this->reservedWords->push_back("else");
    this->reservedWords->push_back("execute");
    this->reservedWords->push_back("buy");
    this->reservedWords->push_back("for");
    this->reservedWords->push_back("money");
    this->reservedWords->push_back("death");
    this->reservedWords->push_back("from");
    this->reservedWords->push_back("defuse_bomb_at");
    this->reservedWords->push_back("with");
    this->reservedWords->push_back("seconds_remaining");
    this->reservedWords->push_back("voip");
    this->reservedWords->push_back("return");
    this->reservedWords->push_back("round_loop");
}

void Tokenizer::fetchTokens()
{
    std::smatch m;
    std::regex e("[0-9]+|(_?[a-zA-Z][_a-zA-Z0-9]*_?)|(==)|(!=)|(::)|(\\,)|(>=)|(<=)|(\\|\\|)|(&&)|(\\.)|(\"[^\"]*\")|[\\+\\-\\/\\*\\(\\)\\=\\\n,.<>!?:;@#$%^&*_~`\\|\\{\\}[\\]]");

    while (std::regex_search(this->source, m, e))
    {
        this->tokens.push_back(m[0]);
        this->source = m.suffix();
    }
    // this->tokens.push_back("GGWP");

#ifdef DEBUG
    for (std::string token : this->tokens)
        std::cout << token << std::endl;
#endif
}

void Tokenizer::selectNext()
{
    bool is_number = true;
    for (char c : tokens[this->position])
        if (!isdigit(c))
            is_number = false;

    if (is_number)
    {
        this->next.type = "NUMBER";
        this->next.value = std::stoi(tokens[this->position]);
    }
    else if (tokens[this->position] == "+")
        this->next.type = "PLUS";
    else if (tokens[this->position] == "-")
        this->next.type = "MINUS";
    else if (tokens[this->position] == "*")
        this->next.type = "MULT";
    else if (tokens[this->position] == "/")
        this->next.type = "DIV";
    else if (tokens[this->position] == ":")
        this->next.type = "COLON";
    else if (tokens[this->position] == "(")
        this->next.type = "LPAREN";
    else if (tokens[this->position] == ")")
        this->next.type = "RPAREN";
    else if (tokens[this->position] == "{")
        this->next.type = "LBRACE";
    else if (tokens[this->position] == "}")
        this->next.type = "RBRACE";
    else if (tokens[this->position] == "GGWP")
        this->next.type = "EOF";
    else if (tokens[this->position] == "=")
        this->next.type = "ASSIGN";
    else if (tokens[this->position] == "known_as")
        this->next.type = "ASSIGN";
    else if (tokens[this->position] == "==")
        this->next.type = "EQUALS";
    else if (tokens[this->position] == "!=")
        this->next.type = "NOTEQUALS";
    else if (tokens[this->position] == "!")
        this->next.type = "NOT";
    else if (tokens[this->position] == ">")
        this->next.type = "GREATERTHAN";
    else if (tokens[this->position] == "<")
        this->next.type = "LESSTHAN";
    else if (tokens[this->position] == ">=")
        this->next.type = "GREATERTHANEQUALS";
    else if (tokens[this->position] == "<=")
        this->next.type = "LESSTHANEQUALS";
    else if (tokens[this->position] == "&&")
        this->next.type = "AND";
    else if (tokens[this->position] == "||")
        this->next.type = "OR";
    else if (tokens[this->position] == "::")
        this->next.type = "DECLARATION";
    else if (tokens[this->position] == ".")
        this->next.type = "CONCAT";
    else if (tokens[this->position] == ",")
        this->next.type = "COMMA";
    else if (std::find(this->reservedWords->begin(), this->reservedWords->end(), tokens[this->position]) != this->reservedWords->end())
    {
        this->next.type = tokens[this->position] == "Int" || tokens[this->position] == "String" ? "TYPE" : tokens[this->position];
        if (tokens[this->position] == "Int" ||
            tokens[this->position] == "String" ||
            tokens[this->position] == "weapon" ||
            tokens[this->position] == "playerID" ||
            tokens[this->position] == "team" ||
            tokens[this->position] == "bombSiteID" ||
            tokens[this->position] == "money" ||
            tokens[this->position] == "round")
        {
            this->next.type = "TYPE";
        }
        else
            this->next.type = tokens[this->position];
        this->next.value = tokens[this->position];
    }
    else if (std::regex_match(tokens[this->position], std::regex("[a-zA-Z0-9_]+")))
    {
        this->next.type = "IDENTIFIER";
        this->next.value = tokens[this->position];
    }
    else if (tokens[this->position].front() == '"' && tokens[this->position].back() == '"')
    {
        this->next.type = "STRING";
        this->next.value = tokens[this->position].substr(1, tokens[this->position].length() - 2);
    }
    else
    {
        this->next.type = "UNKNOWN";
        this->next.value = tokens[this->position];
    }

    this->position++;
}