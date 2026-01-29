from typing import Protocol

# Typage NOMINAL : Dog et Cat sont incompatibles malgré la même structure
class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

def make_dog_speak(dog: Dog) -> str:
    return dog.speak()

# make_dog_speak(Cat())  # ❌ Erreur : Cat n'est pas Dog

# Typage STRUCTURAL avec Protocol : on vérifie la structure, pas le nom
class Speaker(Protocol):
    def speak(self) -> str: ...

def make_speak(animal: Speaker) -> str:
    return animal.speak()

make_speak(Dog())  # ✅ OK : Dog a une méthode speak()
make_speak(Cat())  # ✅ OK : Cat a une méthode speak()
