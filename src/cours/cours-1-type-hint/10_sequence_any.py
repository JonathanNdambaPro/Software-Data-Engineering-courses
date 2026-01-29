import typing as t

def function_with_not_fixed_type(some_sequence: t.Sequence[t.Any]) -> t.Any:
    return some_sequence[1]
