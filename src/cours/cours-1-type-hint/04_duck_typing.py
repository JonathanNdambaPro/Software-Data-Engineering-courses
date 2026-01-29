# Duck typing classique (sans type hints) :
def make_sound(animal):
    print(animal.speak())  # On s'en fiche du type, tant qu'il a une méthode speak()

class Duck:
    def speak(self):
        return "Quack"

class Person:
    def speak(self):
        return "Hello"

make_sound(Duck())    # ✅ Fonctionne
make_sound(Person())  # ✅ Fonctionne aussi !
