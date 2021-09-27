from lispthon.parse import parse
from lispthon.eval import eval

def test_run_program_success():
    program = "(begin (define r 10) (* pi (* r r)))"
    assert eval(parse(program)) == 314.1592653589793