import typing as t

class SomeClass[T]:
    def __init__(self, some_value_generic: T, some_value_generic_bis: T) -> None:
        self.some_value_generic = some_value_generic
        self.some_value_generic_bis = some_value_generic_bis

    def get_values(self) -> tuple[T, T]:
        return (self.some_value_generic, self.some_value_generic_bis)


class SomeClassReturnItSelf:
    def return_self(self) -> t.Self:
        return self


class SomeClassReturnInstance:
    def return_instance(self) -> "SomeClassReturnInstance":
        return SomeClassReturnInstance()
