from typing import *


def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens"
    return chars.replace("(", " ( ").replace(")", " ) ").split()


def atom(token: str) -> Atom:
    "Numbers become numbers, everything else is a symbol"
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


def read_from_tokens(tokens: list) -> Exp:
    "Read expressions from a sequence of tokens"
    if not tokens:
        raise SyntaxError("unexpected EOF")

    token = tokens.pop(0)
    if token == "(":
        L = []
        while tokens[0] != ")":
            L.append(read_from_tokens(tokens))
        tokens.pop(0)  # remove )
        return L
    elif token == ")":
        raise SyntaxError("unexpected )")
    else:
        return atom(token)


def parse(program: str) -> Exp:
    "Return a Scheme expression from a string"
    return read_from_tokens(tokenize(program))
