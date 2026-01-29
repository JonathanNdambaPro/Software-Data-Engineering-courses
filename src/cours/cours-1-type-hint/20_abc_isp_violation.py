from abc import ABC, abstractmethod

class DataHandler(ABC):
    @abstractmethod
    def read(self) -> str:
        pass
    
    @abstractmethod
    def write(self, data: str) -> None:
        pass

# ❌ PROBLÈME : Database peut lire ET écrire
class Database(DataHandler):
    def read(self) -> str:
        return "data from DB"
    def write(self, data: str) -> None:
        print(f"Writing {data} to DB")

# ❌ PROBLÈME : Logger ne peut QUE écrire, pas lire !
# Mais on est OBLIGÉ d'implémenter read() quand même...
class Logger(DataHandler):
    def read(self) -> str:
        raise NotImplementedError("Logger can't read!")  # 😬 Hack moche
    def write(self, data: str) -> None:
        print(f"[LOG] {data}")
