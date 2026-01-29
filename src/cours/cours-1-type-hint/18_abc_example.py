from abc import ABC, abstractmethod

class Serializable(ABC):
    @abstractmethod
    def to_json(self) -> str:
        pass

# ❌ PROBLÈME : On DOIT hériter de Serializable
class User(Serializable):  # Héritage obligatoire !
    def __init__(self, name: str):
        self.name = name
    
    def to_json(self) -> str:
        return f'{{"name": "{self.name}"}}'

# ❌ Impossible d'utiliser une classe qu'on ne contrôle pas
# (ex: une classe d'une librairie externe qui a déjà to_json())
