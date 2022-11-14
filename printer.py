
def pr_str(ast):
    if type(ast) is list:
        return "(" + " ".join([pr_str(e) for e in ast]) + ")"
    else:
        return str(ast)
    