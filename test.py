def foo_maker():
    def foo(*args):
        for k, v in zip(foo.param_names, args):
            print(k, v)
    foo.param_names = ["a", "b"]
    foo.__str__ = "test"
    foo.__repr__ = "test"
    return foo

print(type(foo_maker()))
