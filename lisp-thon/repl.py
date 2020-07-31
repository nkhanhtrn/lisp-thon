from typing import *
from eval import eval
from parse import parse


def scheme_str(exp: Exp) -> str:
    if isinstance(exp, List):
        return "(" + " ".join(map(scheme_str, exp)) + ")"
    else:
        return str(exp)


def repl(prompt="lisp.py> "):
    "A prompt read-eval-input loop"
    while True:
        try:
            val = eval(parse(input(prompt)))
            if val is not None:
                print(scheme_str(val))

        except Exception as e:
            print(e)

