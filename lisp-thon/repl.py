from typing import *
from eval import eval
from parse import parse


def repl(prompt="lisp.py> "):
    "A prompt read-eval-input loop"
    while True:
        val = eval(parse(input(prompt)))
        if val is not None:
            print(schemestr(val))


def schemestr(exp):
    if isinstance(exp, List):
        return "(" + " ".join(map(schemestr(exp))) + ")"
    else:
        return str(exp)
