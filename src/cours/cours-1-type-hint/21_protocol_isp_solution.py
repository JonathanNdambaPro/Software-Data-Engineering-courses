from typing import Protocol

class Readable(Protocol):
    def read(self) -> str: ...

class Writable(Protocol):
    def write(self, data: str) -> None: ...

# Database implémente les DEUX
class Database:
    def read(self) -> str:
        return "data from DB"
    def write(self, data: str) -> None:
        print(f"Writing {data} to DB")

# Logger n'implémente QUE write - et c'est OK !
class Logger:
    def write(self, data: str) -> None:
        print(f"[LOG] {data}")

# ✅ Fonctions qui demandent SEULEMENT ce dont elles ont besoin
def fetch_data(source: Readable) -> str:
    return source.read()

def log_message(dest: Writable, msg: str) -> None:
    dest.write(msg)

def backup(source: Readable, dest: Writable) -> None:
    data = source.read()
    dest.write(data)

# Utilisation
db = Database()
logger = Logger()

fetch_data(db)           # ✅ OK : Database a read()
log_message(logger, "Hello")  # ✅ OK : Logger a write()
log_message(db, "Hello")      # ✅ OK : Database a aussi write()
backup(db, logger)       # ✅ OK : db peut read(), logger peut write()
# fetch_data(logger)       # ❌ Erreur mypy : Logger n'a pas read()
