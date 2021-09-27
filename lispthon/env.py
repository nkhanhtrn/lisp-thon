import math
import operator as op

from .typing import *

class Env(dict):
    def __init__(self):
        self.update(vars(math)) # sin, cos, sqrt, pi...
        self.update({
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": op.truediv,
            ">": op.gt,
            "<": op.lt,
            ">=": op.ge,
            "<=": op.le,
            "=": op.eq,
            "abs": abs,
            "append": op.add,
            "expt": pow,
            "length": len,
            "map": map,
            "max": max,
            "min": min,
            "print": print,
            "round": round,

            "apply": lambda proc, args: proc(*args),
            "begin": lambda *x: x[-1],
            "car": lambda x: x[0],
            "cdr": lambda x: x[1:],
            "cons": lambda x, y: [x] + y,
            "eq?": op.is_,
            "equal?": op.eq,
            "list": lambda *x: List(x),
            "list?": lambda x: isinstance(x, List),
            "not": op.not_,
            "null?": lambda x: x == [],
            "number?": lambda x: isinstance(x, Number),
            "procedure?": callable,
            "symbol?": lambda x: isinstance(x, Symbol),
        })

global_env = Env()
