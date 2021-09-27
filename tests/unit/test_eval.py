import pytest
from lispthon.eval import eval
from lispthon.parse import parse
from lispthon.env import global_env

@pytest.fixture
def env():
    return global_env

def test_eval_operator_add_success(env):
    input = ["+", 1, 1]
    assert eval(input, env) == 2

def test_eval_operator_nested_success(env):
    input = ["+", 1, ['*', 1, 2]]
    assert eval(input, env) == 3

def test_eval_condition_success(env):
    input = ["if", [">", 1, 2], ["+", 1, 2], ["-", 1, 2]]
    assert eval(input, env) == -1

def test_eval_define_variable_success(env):
    input = ["define", "r", ["+", 1, 2]]
    eval(input, env)
    assert env["r"] == 3