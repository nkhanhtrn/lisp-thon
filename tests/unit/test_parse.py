import pytest
from lispthon.parse import parse

def test_parse_success():
    assert parse("(+ 1 1)") == ["+", 1, 1]

def test_parse_nested_syntax_success():
    program = "(begin (define r 10) (* pi (* r r)))"
    result = ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]
    assert parse(program) == result

def test_parse_extra_open_parens():
    with pytest.raises(SyntaxError):
        parse("(+ 1 1 ")

def test_parse_extra_close_parens():
    with pytest.raises(SyntaxError):
        parse("(+ 1 1))")