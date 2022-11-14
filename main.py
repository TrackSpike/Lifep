import sys, traceback
from custom_types import Symbol
from env import Env
from printer import pr_str
from reader import read_str

std_env = Env(None)
std_env.set('+', lambda a,b: a+b)
std_env.set('-', lambda a,b: a-b)
std_env.set('*', lambda a,b: a*b)
std_env.set('/', lambda a,b: int(a/b))


def READ(p):
    return read_str(p)


def EVAL(p, env):
    if type(p) == list:
        if not p:
            return p
        elif type(p[0]) == Symbol:
            return apply(p, env)
        else:
            return eval_ast(p, env)
    else:
        return eval_ast(p, env)

def apply(p, env):
    # Handle Special Atoms
    if p[0].value == "def!":
        env.set(p[1].value, EVAL(p[2], env))
        return env.get(p[1].value)
    elif p[0].value == "let*":
        new_env = Env(env)
        defs = p[1]
        i = 0
        while i < len(defs):
            new_env.set(defs[i].value, EVAL(defs[i+1], new_env))
            i += 2
        return EVAL(p[2], new_env)
    # Default
    else:
        p = eval_ast(p, env)
        return p[0](*p[1:])

def PRINT(p):
    return pr_str(p)


def rep(p):
    return PRINT(EVAL(READ(p), std_env))

def eval_ast(ast, env):
    t = type(ast)
    if t == Symbol:
        return env.get(ast.value)
    elif t == list:
        return [EVAL(e, env) for e in ast]
    else:
        return ast

def main():
    while True:
        try:
            line = input("user>")
            if line == None:
                break
            elif line == "":
                continue
            else:
                print(rep(line))
        except Exception:
            print("".join(traceback.format_exception(*sys.exc_info())))


if __name__ == "__main__":
    main()
