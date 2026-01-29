import typing as t

type FunctionBluePrintStr = t.Callable[[str, str], str | list[str]]


def some_function(value_1: str, value_2: str) -> str:
    return value_1 + value_2


def some_function_bis(value_1: str, value_2: str) -> list[str]:
    return [value_1, value_2]


dict_value: FunctionBluePrintStr = {
    "some_key": some_function,
    "some_key_bis": some_function_bis,
}
