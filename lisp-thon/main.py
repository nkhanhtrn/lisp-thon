Symbol = str
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict


def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens"
    return chars.replace("(", " ( ").replace(")", " ) ").split()


if __name__ == "__main__":
    program = "(begin (define r 10) (* pi (* r r)))"
    print(tokenize(program))
