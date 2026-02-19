# Exercice : Convertir des classes en dataclasses
# Convertissez les classes suivantes en dataclasses de manière à ce que
# les initialisateurs générés aient le même comportement que la classe classique.


class A:
    def __init__(self) -> None:
        self._length = 0


class B:
    def __init__(self, x: int, y: str = "hello", values: list[int] | None = None) -> None:
        self.x = x
        self.y = y
        self.values = values if values else []


class C:
    def __init__(self, a: int = 3) -> None:
        self.a = a
        self.b = a + 3
