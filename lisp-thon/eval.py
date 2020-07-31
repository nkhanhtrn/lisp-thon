from typing import *
from env import global_env


def eval(x: Exp, env=global_env) -> Exp:
    if isinstance(x, Symbol):
        return env.find(x)
    elif isinstance(x, Number):
        return x

    op, *args = x

    if op == "if":
        (test, conseq, alt) = args
        exp = conseq if eval(test, env) else alt
        return eval(exp, env)
    elif op == "define":
        (symbol, exp) = args
        env[symbol] = eval(exp, env)
    elif op == "quote":
        return args[0]
    elif op == "set!":
        (symbol, exp) = args
        if symbol not in env:
            raise ValueError("{} is not defined".format(symbol))
        env[symbol] = eval(exp, env)
    elif op == "lambda":
        (params, body) = args
        return Procedure(params, body, env)
    else:
        proc = eval(op, env)
        vals = [eval(arg, env) for arg in args]
        return proc(*vals)


class Procedure:
    def __init__(self, params, body, env: Env):
        self.params, self.body, self.env = params, body, env

    def __call__(self, *args):
        return eval(self.body, Env(self.params, args, self.env))
