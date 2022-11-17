
import types


def pr_str(ast):
    if type(ast) is list:
        return "(" + " ".join([pr_str(e) for e in ast]) + ")"
    else:
        return toStr(ast)
    
def toStr(obj):
    if isinstance(obj, types.FunctionType):
        return "Function"
    else:
        return str(obj)