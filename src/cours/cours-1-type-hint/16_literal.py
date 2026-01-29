import typing as t

type Mode = t.Literal["r", "rb", "w", "wb"]

def open_helper(file: str, mode: Mode) -> str: ...
