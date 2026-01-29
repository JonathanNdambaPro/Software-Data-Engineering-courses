import typing as t

@t.runtime_checkable
class Closable(t.Protocol):
    def close(self): ...


class SomeClassCheckable:
    def close(self):
        print("lol")

isinstance(SomeClassCheckable(), Closable)
