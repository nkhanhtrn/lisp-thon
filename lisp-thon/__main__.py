from parse import parse
from env import global_env
from eval import eval

program = "(begin (define r 10) (* pi (* r r)))"
print(eval(parse(program)))
