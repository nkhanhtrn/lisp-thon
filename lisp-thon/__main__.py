from parse import parse


program = "(begin (define r 10) (* pi (* r r)))"
print(parse(program))
