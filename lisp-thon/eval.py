from typing import *
from env import global_env as env

# ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]


def eval(x: Exp) -> Exp:
    if isinstance(x, Symbol):
        return env[x]
    elif isinstance(x, Number):
        return x
    elif x[0] == "if":
        (_, test, conseq, alt) = x
        exp = conseq if eval(test) else alt
        return eval(exp)
    elif x[0] == "define":
        (_, symbol, exp) = x
        env[symbol] = eval(exp)
    else:
        proc = eval(x[0])
        args = [eval(arg) for arg in x[1:]]
        return proc(*args)
