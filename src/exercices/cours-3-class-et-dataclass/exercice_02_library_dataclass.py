# Exercice : Système de gestion de bibliothèque
# Créez un système de gestion de bibliothèque en utilisant les dataclasses.
#
# 1. Créez un enum `Genre` avec les valeurs : FICTION, NON_FICTION, SCIENCE, HISTORY, TECHNOLOGY
#
# 2. Créez une dataclass `Book` avec :
#    - title (str)
#    - author (str)
#    - genre (Genre)
#    - isbn (str)
#    - pages (int)
#    - available (bool, par défaut True)
#    - Utilisez `order=True` pour permettre le tri des livres par titre
#    - Utilisez `frozen=True` pour l'immuabilité (les infos d'un livre ne devraient pas changer)
#
# 3. Créez une dataclass `Library` avec :
#    - name (str)
#    - books : liste de Book (utilisez default_factory)
#    - Une méthode `add_book(book)` qui ajoute un livre à la bibliothèque
#    - Une méthode `find_by_genre(genre)` qui retourne tous les livres d'un genre donné
#    - Une méthode `find_by_author(author)` qui retourne tous les livres d'un auteur donné
#
# 4. Dans main() :
#    - Créez une Library
#    - Ajoutez au moins 4 livres de genres différents
#    - Trouvez tous les livres d'un genre spécifique
#    - Triez les livres par titre avec sorted()
#    - Affichez les résultats
