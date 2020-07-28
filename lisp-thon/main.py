Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict


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
        tokens.pop(0)
        return L
    elif token == ")":
        raise SyntaxError("unexpected )")
    else:
        return atom(token)


def parse(program: str) -> Exp:
    "Return a Scheme expression from a string"
    return read_from_tokens(tokenize(program))


if __name__ == "__main__":
    program = "(begin (define r 10) (* pi (* r r)))"
    print(parse(program))
