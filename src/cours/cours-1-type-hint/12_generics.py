import typing as t

U = t.TypeVar("U")


def func_typevar(some_sequence: t.Sequence[U]) -> U:
    return some_sequence[1]

def func_typevar_second_version[T](some_sequence: t.Sequence[T]) -> T:
    return some_sequence[1]

def some_function_add_type_var_simpler(value_1: U, value_2: U) -> U:
    return value_1 + value_2

def some_function_add_type_var_compact[G](value_1: G, value_2: G) -> G:
    return value_1 + value_2
