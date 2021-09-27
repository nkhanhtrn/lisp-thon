from .typing import *
from .env import global_env

def eval(x: Expression, env=global_env) -> Expression:
    if isinstance(x, Symbol):
        return env[x]
    elif isinstance(x, Number):
        return x

    operator, *args = x
    if operator == "if": # (if (> 10 20) (+ 1 1) (+ 3 3))
        condition, if_works, else_works = args
        works = if_works if eval(condition, env) else else_works
        return eval(works, env)

    elif operator == "define": # (define r 10)
        symbol, expression = args
        env[symbol] = eval(expression)
        
    else: # predefined function call
        values = [eval(arg, env) for arg in args]
        return env[operator](*values)
