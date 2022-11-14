class Symbol:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return self.value

class BooleanAtom:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)