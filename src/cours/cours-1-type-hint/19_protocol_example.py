from typing import Protocol

class Serializable(Protocol):
    def to_json(self) -> str: ...

# ✅ Pas besoin d'hériter ! La classe doit juste avoir to_json()
class User:  # Pas d'héritage
    def __init__(self, name: str):
        self.name = name
    
    def to_json(self) -> str:
        return f'{{"name": "{self.name}"}}'

# ✅ Fonctionne aussi avec des classes existantes (librairies externes)
class ExternalApiResponse:  # Imaginons une classe d'une lib externe
    def to_json(self) -> str:
        return '{"status": "ok"}'

def save_to_file(obj: Serializable) -> None:
    with open("data.json", "w") as f:
        f.write(obj.to_json())

save_to_file(User("Alice"))           # ✅ OK
save_to_file(ExternalApiResponse())   # ✅ OK aussi !
