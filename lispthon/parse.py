from .typing import *

def tokenize(chars: str) -> list:
    "Convert a string of characters into a iterable list of tokens"
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

def validate(programs: str):
    "validate parenthesis count"
    parens_count = 0
    for char in programs:
        if char == "(":
            parens_count += 1
        elif char == ")":
            parens_count -= 1

    if parens_count > 0:
        raise SyntaxError("Extra ( detected")
    if parens_count < 0:
        raise SyntaxError("Extra ) detected")


def build_ast(tokens: iter) -> Expression:
    "Read expressions from a sequence of tokens"
    token = next(tokens, None)
    tree = []
    while token is not None and token != ")":
        if token == "(":
            tree.append(build_ast(tokens))
        else:
            tree.append(atom(token))

        token = next(tokens, None)
    
    return tree


def parse(program: str) -> Expression:
    "Return a Scheme expression from a string"
    validate(program)
    tokens = tokenize(program)
    return  build_ast(iter(tokens))