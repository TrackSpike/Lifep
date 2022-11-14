import re
from custom_types import Symbol

class Reader:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def next(self):
        v = self.tokens[self.position]
        self.position += 1
        return v

    def peek(self):
        return self.tokens[self.position]

def read_str(inputStr):
    reader = Reader(tokenize(inputStr))
    return read_form(reader)

def tokenize(inputStr):
    key = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""");
    return re.findall(key, inputStr)

def read_form(reader):
    token = reader.peek()
    if token == "(":
        return read_list(reader)
    elif token == ")":
        raise Exception(f"Unexpected ) at pos {reader.position}")
    else:
        return read_atom(reader)

def read_list(reader):
    reader.next()
    result = []
    while reader.peek() != ")":
        result.append(read_form(reader))
    reader.next()
    return result
 
def read_atom(reader):
    token = reader.next()
    isNum = re.compile(r'\d+(?:.\d*)?')
    if token == "None":
        return None
    if token == "True":
        return True
    elif token == "False":
        return False
    elif isNum.match(token):
        return int(token)
    else:
        return Symbol(token)