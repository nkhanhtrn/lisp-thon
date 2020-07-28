from typing import *
from eval import eval, scheme_str
from parse import parse


def repl(prompt="lisp.py> "):
    "A prompt read-eval-input loop"
    while True:
        try:
            val = eval(parse(input(prompt)))
            if val is not None:
                print(scheme_str(val))

        except Exception as e:
            print(e)
