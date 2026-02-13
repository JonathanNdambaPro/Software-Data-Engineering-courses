# Data structure

## Numerical

Il y a les entiers, les flottants et les décimaux qui sont une version plus précise que les flottants.

On peut facilement convertir des flottants en entiers et inversement.

```python
--8<-- "src/cours/cours-2-datastructure/01_conversion_int_float.py"
```

### Integer

Les entiers dans Python ont une taille de représentation limitée uniquement par la mémoire RAM (contrairement à Java ou C# qui ont une taille de représentation soit de 32 bits soit de 64 bits). Cela permet d'avoir des entiers très longs et très précis, mais la représentation de ce nombre peut varier en fonction de la RAM disponible entre deux PC si le nombre est extrêmement long.

Le fait que les entiers sont limités uniquement par la mémoire RAM implique que si le nombre est vraiment grand, il peut ralentir le système et donc la vitesse des opérations de calcul.

Si le nombre est vraiment très grand, l'ordinateur pourrait même ne plus fonctionner.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/02_integer_examples.py"
```


### Flottant

Les flottants ont une précision fixe, ce qui veut dire qu'à partir d'une certaine taille Python va tronquer l'excédent. Cela peut conduire à une propagation d'erreurs qui est souvent négligeable pour la majorité des cas d'usage mais catastrophique pour les calculs de haute précision.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/03_float_precision.py"
```

### Decimal

C'est une solution qui permet d'être plus précis avec les nombres décimaux en les exprimant sous forme de fraction. Les Decimal couvrent la majorité des cas mais en contrepartie sont plus lents que les flottants.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/04_decimal_precision.py"
```


## String

Pour les strings, on peut utiliser des guillemets simples (single quotes) ou des guillemets doubles (double quotes), cela n'a pas vraiment d'importance.

```python
--8<-- "src/cours/cours-2-datastructure/05_quotes_simple_double.py"
```

On peut aussi utiliser plusieurs quotes (triple quotes) pour faire du texte multi-ligne.

```python
--8<-- "src/cours/cours-2-datastructure/06_multiline_strings.py"
```

Les strings contiennent plusieurs opérations en commun avec les listes (concaténation, slicing, index).

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/07_string_operations.py"
```

Contrairement aux listes, les strings sont immutables.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/08_string_immutability.py"
```

### F string

Les f-strings (formatted string literals) permettent d'insérer des variables et des expressions directement dans une string en utilisant le préfixe `f` et des accolades `{}`. C'est la méthode la plus moderne et lisible pour formater des strings en Python (introduite en Python 3.6).

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/09_fstring_examples.py"
```

## Booleen

Les booléens sont simples : ils ne sont composés que de deux valeurs `True` et `False`. Ces deux valeurs ont des équivalents entiers `1` et `0` car au final `True` et `False` sont des sous-classes d'entiers et donc sont des entiers.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/10_boolean_examples.py"
```

## Enum

Les Enums (énumérations) permettent de créer des ensembles de constantes nommées. Elles rendent le code plus lisible et moins sujet aux erreurs qu'avec des constantes simples ou des strings magiques.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/11_enum_examples.py"
```

## List

Les listes sont des séquences mutables et ordonnées d'éléments. Pour faire simple, chaque élément peut être modifié et possède un index fixe. Les éléments d'une liste ne sont pas obligés d'être du même type et la taille maximale d'une liste dépend uniquement de la taille de la RAM, donc potentiellement infinie.

Les listes se redimensionnent automatiquement et peuvent donc conduire à des problèmes de mémoire. Si les éléments sont trop différents, les opérations sur les différents éléments peuvent devenir complexes. Si on a besoin d'une structure avec beaucoup de types de données différentes, les classes sont mieux adaptées.

Les recherches dans une liste peuvent être longues ; pour des recherches très fréquentes, les dictionnaires sont plus adaptés.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/12_list_operations.py"
```

## Array

Les arrays sont moins flexibles et plus basiques que les listes. Elles ont une taille fixe ce qui permet un accès bien plus rapide aux éléments car une mémoire leur est allouée. On utilise souvent NumPy pour les arrays.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/13_array_examples.py"
```

## Dictionary

Pour la recherche, rien n'est plus rapide que les dictionnaires car ils utilisent une table de hachage (hash table).

Les dictionnaires sont ordonnés depuis Python 3.7+ (ordre d'insertion) et ont besoin de plus de mémoire.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/14_dict_operations.py"
```

## Tuple

Les tuples sont des collections d'objets immuables. Comparés aux listes, ils ont un accès bien plus rapide aux éléments. Ils sont beaucoup utilisés pour le packing et l'unpacking de variables. Ils peuvent aussi être utilisés pour des match/case avec des valeurs complexes. Cependant, si la structure devient trop complexe, il faudra migrer vers une classe.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/15_tuple_examples.py"
```

## Set

Les sets permettent d'avoir une collection d'éléments uniques. Ils sont mutables et non ordonnés. Ils sont facilement convertibles et peuvent donc servir d'outil de dédoublonnage avant d'être réutilisés.

Si on a besoin d'un set immutable, on peut utiliser des frozensets.

**Exemples:**

```python
--8<-- "src/cours/cours-2-datastructure/16_set_operations.py"
```
