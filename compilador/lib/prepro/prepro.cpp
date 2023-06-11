#include "prepro.hpp"
#include <regex>

void Prepro::filter(std::string &code)
{
    // std::regex e("#.*");
    // code = std::regex_replace(code, e, "");
    // replace \n with space
    std::regex e("\n");
    code = std::regex_replace(code, e, " ");
}