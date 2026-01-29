# Type Hint

Des langages comme Java, C# ou encore C++ ont des types dans leur syntaxe. Python n'en a pas, ce qui peut engendrer des erreurs.

## Pourquoi utilise-t-on les types ?

Les types permettent de faciliter la lecture du code ; c'est une sorte de documentation. Ils peuvent également permettre à des "static type checkers" (vérificateurs de type statiques) de vérifier s'il n'y a pas d'erreur de type.

Ils aident les développeurs avec qui vous travaillez à mieux savoir ce qui est attendu en entrée et en sortie.

## Les différents types de typage

### Static vs Dynamic

**Typage statique** : Les types sont vérifiés **à la compilation** (avant l'exécution). Si une erreur de type existe, le programme ne compile pas.  
Exemples : Java, C#, C++, TypeScript

**Typage dynamique** : Les types sont vérifiés **à l'exécution**. Une erreur de type ne sera détectée que lorsque le code problématique est exécuté.  
Exemples : Python, JavaScript, Ruby

```python
--8<-- "src/cours/cours-1-type-hint/01_dynamic_vs_static.py"
```

> Python est un langage **dynamiquement typé**, mais les *type hints* permettent d'ajouter une vérification "statique" grâce à des outils comme `mypy` ou `pyright`.

### Manifest vs Inferred

**Manifest (explicite)** : Le développeur doit déclarer explicitement les types dans le code.  
Exemples : Java, C (`int x = 5;`)

**Inferred (inféré)** : Le compilateur/interpréteur déduit automatiquement le type à partir de la valeur.  
Exemples : TypeScript, Kotlin, Python avec type hints (`x = 5` → le type `int` est inféré)

```python
--8<-- "src/cours/cours-1-type-hint/02_manifest_vs_inferred.py"
```

> Python supporte les deux : on peut écrire `x: int = 5` (manifest) ou laisser l'outil inférer le type.


### Nominal vs Structural

**Nominal** : Deux types sont compatibles uniquement s'ils ont le **même nom** (ou une relation d'héritage explicite).  
Exemples : Java, C# — `class Dog` et `class Cat` sont incompatibles même s'ils ont les mêmes attributs.

**Structural** : Deux types sont compatibles s'ils ont la **même structure** (mêmes attributs/méthodes), peu importe leur nom.  
Exemples : TypeScript, Go — si deux objets ont les mêmes propriétés, ils sont compatibles.

```python
--8<-- "src/cours/cours-1-type-hint/03_nominal_vs_structural.py"
```

> Python avec les *type hints* utilise principalement le typage **nominal**, mais les `Protocol` permettent un typage **structural** (duck typing vérifié statiquement).

### Duck Typing 🦆

Le **duck typing** est la philosophie de Python :

> *"If it walks like a duck and quacks like a duck, then it must be a duck."*  
> (Si ça marche comme un canard et ça fait coin-coin comme un canard, alors c'est un canard.)

En pratique : on ne vérifie pas le **type** d'un objet, mais s'il possède les **méthodes/attributs** dont on a besoin.

```python
--8<-- "src/cours/cours-1-type-hint/04_duck_typing.py"
```

> ⚠️ **Problème** : Les erreurs ne sont détectées qu'à l'exécution. Si on passe un objet sans méthode `speak()`, on aura une `AttributeError` au runtime.  
> **Solution** : Utiliser `Protocol` (voir section précédente) pour combiner duck typing + vérification statique.


## Compiled vs Interpreted

**Langage compilé** : Le code source est traduit **entièrement** en code machine (binaire) par un compilateur **avant** l'exécution. Le résultat est un exécutable autonome.  
Exemples : C, C++, Rust, Go

**Langage interprété** : Le code source est lu et exécuté **ligne par ligne** par un interpréteur au moment de l'exécution.  
Exemples : JavaScript (historiquement), Bash

> **Et Python ?** Python est un cas hybride : le code est d'abord **compilé en bytecode** (fichiers `.pyc`), puis ce bytecode est **interprété** par la machine virtuelle Python (CPython). On dit souvent que Python est "interprété" car cette compilation est transparente pour l'utilisateur.

### Avantages et inconvénients

| Type | Avantages | Inconvénients |
|------|-----------|---------------|
| **Compilé** | Exécution très rapide, optimisations du compilateur, erreurs détectées avant l'exécution | Temps de compilation, moins portable (dépend de l'architecture), cycle de développement plus long |
| **Interprété** | Développement rapide (modifier → relancer), plus portable, debugging plus facile | Exécution plus lente, erreurs détectées seulement à l'exécution |

## Lien entre compilation/interprétation et typage

Le choix du système de typage (statique vs dynamique) est souvent lié au mode d'exécution du langage :

**Langages compilés → souvent typés statiquement**  
Le compilateur a besoin de connaître les types à l'avance pour générer du code machine optimisé. Connaître le type permet d'allouer la bonne quantité de mémoire et d'utiliser les bonnes instructions CPU.

**Langages interprétés → souvent typés dynamiquement**  
L'interpréteur peut inspecter les valeurs au moment de l'exécution, ce qui permet plus de flexibilité (ex: une variable peut changer de type en cours de route).

> ⚠️ **Attention** : Ce n'est pas une règle absolue ! TypeScript est compilé mais transpilé en JavaScript. Go est compilé et statiquement typé mais avec de l'inférence de types. Python est interprété mais supporte les type hints vérifiés statiquement.

## Quand utiliser le typing en Python

Une mauvaise pratique est de l'utiliser quand on définit une variable. C'est de l'over-engineering car c'est déjà facile à comprendre :

```python
--8<-- "src/cours/cours-1-type-hint/05_bad_practice_variable_hinting.py"
```

Le typage est particulièrement utile pour la définition de fonctions et de méthodes :

```python
--8<-- "src/cours/cours-1-type-hint/06_function_typing.py"
```

Même avec une valeur par défaut, il est tout de même conseillé d'ajouter le typage :

```python
--8<-- "src/cours/cours-1-type-hint/07_default_values.py"
```

Les classes peuvent aussi être considérées comme un type :

```python
--8<-- "src/cours/cours-1-type-hint/08_classes_as_types.py"
```

> ⚠️ **Attention** : Dans la vraie vie `print_car` devrait être une méthode de la classe pour ne pas violer le principe de `Principle of Least Knowledge (Law of Demeter)`

> ⚠️ **Attention** : `int | float` veut dire que l'argument peut être un entier ou un flottant

## Les typings exotiques

### Sequence

`Sequence` est un type très utile pour représenter toute structure de donnée ordonnée et indexable (comme `list`, `tuple`, `str`), mais de manière **immmuable** (on ne peut pas modifier les éléments, juste les lire).

C'est souvent préférable à `list` si votre fonction a juste besoin de lire des éléments, car cela rend votre fonction compatible avec plus de types (ex: tuples).

```python
--8<-- "src/cours/cours-1-type-hint/09_sequence_fixed.py"
```

Si le contenu de la séquence peut être de n'importe quel type, on peut utiliser `Any` :

```python
--8<-- "src/cours/cours-1-type-hint/10_sequence_any.py"
```

### L'Union

L'opérateur `|` (ou `Union` dans les anciennes versions de Python) permet de spécifier qu'une variable peut accepter **plusieurs types différents**.

Par exemple, si une fonction peut prendre un entier OU un nombre flottant :

```python
--8<-- "src/cours/cours-1-type-hint/11_union.py"
```

### Type générique (TypeVar)

Les génériques permettent d'écrire des fonctions flexibles qui acceptent différents types tout en maintenant une relation stricte entre eux.

Si vous utilisez `Any`, vous perdez l'information de type. Avec un `TypeVar`, vous dites : "Je ne sais pas quel est ce type *T*, mais si tu me donnes une liste de *T*, je te renverrai un *T*".

Exemple : 
- Si l'entrée est `list[str]`, la sortie sera `str`.
- Si l'entrée est `list[int]`, la sortie sera `int`.

```python
--8<-- "src/cours/cours-1-type-hint/12_generics.py"
```

### Callable

`Callable` est utilisé pour typer des fonctions passées en argument (callbacks). La syntaxe est `Callable[[Arg1Type, ArgType2], ReturnType]`.

#### Python < 3.13 (Syntaxe classique)

```python
--8<-- "src/cours/cours-1-type-hint/13_callable_old.py"
```

#### Python >= 3.12 (Nouvelle syntaxe `type`)

Depuis Python 3.12, on peut utiliser le mot-clé `type` pour créer des alias de type plus lisibles.

```python
--8<-- "src/cours/cours-1-type-hint/14_callable_new.py"
```

### Classe et Générique

On peut aussi créer des classes génériques. Cela est très courant pour des structures de données (comme une Pile, une File, ou un Wrapper).

L'exemple ci-dessous montre :
1. Une classe générique `SomeClass[T]`
2. L'usage de `Self` pour indiquer qu'une méthode retourne l'instance elle-même (utile pour le "method chaining" ou les patterns Builder).
3. La différence avec le typage par chaîne de caractères (forward reference).

Exemple :
- `SomeClass[str]` (ou `SomeClass("a", "b")`) : `T` devient `str`, donc `get_values()` retournera un tuple de strings.
- `SomeClass[int]` (ou `SomeClass(1, 2)`) : `T` devient `int`, donc `get_values()` retournera un tuple d'entiers.

```python
--8<-- "src/cours/cours-1-type-hint/15_class_generics_self.py"
```

### Literal

`Literal` permet de restreindre une valeur non pas à un type, mais à un **ensemble précis de valeurs**. C'est très utile pour les modes d'ouverture de fichiers, les statuts, ou les options de configuration.

```python
--8<-- "src/cours/cours-1-type-hint/16_literal.py"
```

### Protocol checkable

Par défaut, les `Protocol` sont vérifiés uniquement par les outils d'analyse statique (mypy). Si vous voulez vérifier si un objet respecte un protocole **au moment de l'exécution** (avec `isinstance`), vous devez décorer votre protocole avec `@runtime_checkable`.

```python
--8<-- "src/cours/cours-1-type-hint/17_runtime_checkable.py"
```


## Protocol vs Abstract Base Class (ABC)

Les **classes abstraites** (`ABC`) et les **Protocols** permettent tous deux de définir des "contrats" que d'autres classes doivent respecter. Mais ils ont des différences fondamentales :

| Aspect | ABC | Protocol |
|--------|-----|----------|
| Héritage requis | ✅ Oui, obligatoire | ❌ Non (structural) |
| Vérification | À l'exécution | Statique (mypy) |
| Compatible avec code existant | ❌ Non | ✅ Oui |
| Peut définir des implémentations | ✅ Oui | ❌ Non (juste signatures) |

#### Exemple avec ABC (classe abstraite)

```python
--8<-- "src/cours/cours-1-type-hint/18_abc_example.py"
```

#### Exemple avec Protocol (typage structural)

```python
--8<-- "src/cours/cours-1-type-hint/19_protocol_example.py"
```

> 💡 **Quand utiliser quoi ?**
> - **ABC** : Quand tu veux forcer un héritage explicite et fournir des implémentations par défaut
> - **Protocol** : Quand tu veux de la flexibilité (duck typing vérifié) et compatibilité avec du code existant

#### Le vrai pouvoir de Protocol : la composition

Imaginons qu'une ABC définisse **2 méthodes**, mais que certaines classes n'en implémentent qu'**une seule** :

```python
--8<-- "src/cours/cours-1-type-hint/20_abc_isp_violation.py"
```

Avec **Protocol**, on peut définir des contrats **séparés et composables** :

```python
--8<-- "src/cours/cours-1-type-hint/21_protocol_isp_solution.py"
```

> 🎯 **Principe clé** : Avec Protocol, chaque fonction demande **uniquement** les méthodes dont elle a besoin. C'est l'**Interface Segregation Principle** (SOLID) appliqué naturellement !
