from env import Env

std_lib = {
    '=': lambda a, b: a == b,
    '<': lambda a, b: a < b,
    '<=': lambda a, b: a <= b,
    '>': lambda a, b: a > b,
    '>=': lambda a, b: a >= b,
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b,
    '*': lambda a, b: a*b,
    '/': lambda a, b: int(a/b),
    'list': lambda *args: list(args),
    'list?': lambda *args: type(args[0]) == list,
    'empty?': lambda *args: len(args[0]) == 0,
    'count': lambda *args: len(args[0]),
}

std_env = Env(None,std_lib)
