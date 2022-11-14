class Env:
    def __init__(self, outer):
        self.outer = outer
        self.data = {}
    
    def set(self, key, value):
        self.data[key] = value

    def find(self, key):
        if key in self.data:
            return self
        elif self.outer:
            return self.outer.find(key)
        else:
            return None
    
    def get(self, key):
        env = self.find(key)
        if not env:
            raise Exception(f"Cannot find {key}")
        return self.data[key]