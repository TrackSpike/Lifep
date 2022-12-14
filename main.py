import sys
import traceback
import types
from custom_types import Symbol
from env import Env
from printer import pr_str
from reader import read_str
from core import std_env

def READ(p):
    return read_str(p)


def EVAL(p, env):
    if type(p) == list:
        if not p:
            return p
        elif type(p[0]) == Symbol:
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
            elif p[0].value == "do":
                last = None
                for e in p[1:]:
                    last = eval_ast(e, env)
                return last
            elif p[0].value == "if":
                condition = EVAL(p[1], env)
                if condition != None and condition != False:
                    return EVAL(p[2], env)
                elif len(p) > 3:
                    return EVAL(p[3], env)
                else:
                    return None
            elif p[0].value == "fn*":
                return build_closure(p[1], p[2], env)
            else:
                p = eval_ast(p, env)
                return p[0](*p[1:])
        else:
            p = eval_ast(p, env)
            if isinstance(p[0], types.FunctionType):
                return p[0](*p[1:])
            else:
                return p
    else:
        return eval_ast(p, env)


def build_closure(params, body, env):
    def closure(*args):
        new_env = Env(env, keys={e[0]:e[1] for e in zip(closure.__argNames__, args)})
        return EVAL(body, new_env)
    closure.__argNames__ = [p.value for p in params]
    return closure


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
