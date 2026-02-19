# Class et Dataclass

## Introduction

Une classe est un **blueprint** d'un objet. Elle spécifie ce qu'il se passe quand on crée un objet, comment on accède à ses parties et quels comportements il possède.

Dans Python, tout est un objet. Les fonctions, par exemple, sont des **callable**.

Les classes sont plus concentrées sur les **behaviors** (méthodes) plutôt que sur les **données** (attributs). Les dataclasses, c'est le contraire.

## Les classes et les méthodes dunder

```python
--8<-- "src/cours/cours-3-class-et-dataclass/01_dunder_methods_comparisons.py"
```

On peut ajouter de plus en plus de méthodes et faire d'elle une "God" classe, ce qui est à éviter. Ici, une bonne idée serait de séparer les données des méthodes.

En général, les classes sont particulièrement utiles pour représenter une sorte de données structurées plutôt qu'un ensemble de méthodes.

## Les dataclasses

La force des dataclasses, c'est qu'elles ont moins de **boilerplate code**, en particulier dans l'initialisateur. Comme on peut le voir, les dataclasses sont bien plus faciles à lire et on peut les appliquer directement :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/02_dataclass_bank_account.py"
```

### `__repr__` natif

Les dataclasses ont aussi nativement plusieurs méthodes dunder préparées, comme `__repr__` pour `print` :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/03_dataclass_vehicle.py"
```

### Comparaison des méthodes dunder

On peut aller encore plus loin dans la comparaison des méthodes dunder entre une classe classique et une dataclass :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/04_pydantic_alternative.py"
```

### `order=True`

Avec `order=True`, on ajoute automatiquement les méthodes de comparaison (`__lt__`, `__le__`, `__gt__`, `__ge__`) :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/05_dataclass_order.py"
```

## Fonctionnalités avancées

### `default_factory`

Il est possible d'utiliser `default_factory` qui permet d'initialiser une liste (ou tout autre objet mutable) sans que les objets pointent sur la même référence, vu que Python fonctionne par référence. Pydantic gère cela nativement.

`default_factory` ne marche pas que pour les listes, mais pour tous les types mutables (dict, set, etc.) :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/06_default_factory.py"
```

### Options de `field()` et `__post_init__`

Les dataclasses peuvent aussi ajouter plusieurs autres fonctionnalités nativement ou les enlever grâce aux options de `field()` (`compare`, `init`, `repr`) et à la méthode `__post_init__` :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/07_dataclass_advanced.py"
```

### `frozen=True`

On peut également ajouter `frozen=True` pour rendre les attributs **immuables**. Toute tentative de modification lèvera une `FrozenInstanceError` :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/08_frozen_dataclass.py"
```

### `slots=True`

Si on a besoin de plus de **performance**, on peut utiliser `slots=True`. C'est une optimisation de Python : une dataclass est finalement un dictionnaire (accessible via `__dict__`). Quand on utilise `slots`, on dit à Python de n'allouer de l'espace mémoire uniquement pour les attributs définis, sans utiliser de dictionnaire interne :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/09_slots_dataclass.py"
```

La principale faiblesse de `slots` est qu'on ne peut pas allouer de variables dynamiquement.

## Alternatives : Pydantic

Il existe des alternatives comme **Pydantic** qui permet de faire des validations et de s'intégrer facilement à des APIs modernes comme **FastAPI**. Il faut par contre faire attention : Pydantic est une dépendance externe et prend plus de temps que les classes ou les dataclasses à s'initialiser. Si on construit un module de bas niveau (comme de l'open source) et qu'il y a des critères de vitesse, il n'est pas souhaitable de l'utiliser.

### Validation et coercion de types

Pydantic valide automatiquement les types et permet de définir des **contraintes** via `Field` (`min_length`, `gt`, `lt`, etc.). Il effectue aussi de la **coercion de types** (par exemple, convertir `"25"` en `25`) :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/10_pydantic_validation.py"
```

### Validators personnalisés

Avec `@field_validator`, on peut transformer et valider chaque champ individuellement. Avec `@model_validator`, on peut faire de la **validation croisée** entre plusieurs champs :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/11_pydantic_validators.py"
```

### Sérialisation et désérialisation

Pydantic gère nativement les **modèles imbriqués** et la **sérialisation** (`model_dump`, `model_dump_json`) / **désérialisation** (`model_validate`, `model_validate_json`), ce qui est particulièrement utile pour les APIs :

```python
--8<-- "src/cours/cours-3-class-et-dataclass/12_pydantic_serialization.py"
```

## Exercices

### Exercice 1 : From Class to Dataclass

Convertir les classes suivantes en dataclasses de manière à ce que les initialisateurs générés aient le même comportement que la classe classique :

```python
--8<-- "src/exercices/cours-3-class-et-dataclass/exercice_01_class_to_dataclass.py"
```

### Exercice 2 : Système de gestion de bibliothèque (Dataclass)

Créer un système de gestion de bibliothèque en utilisant les dataclasses avec `order`, `frozen`, `default_factory` et les enums :

```python
--8<-- "src/exercices/cours-3-class-et-dataclass/exercice_02_library_dataclass.py"
```

### Exercice 3 : Validation d'inscription utilisateur (Pydantic)

Créer un système de validation d'inscription avec `@field_validator`, les contraintes `Field`, et la sérialisation :

```python
--8<-- "src/exercices/cours-3-class-et-dataclass/exercice_03_pydantic_registration.py"
```

### Exercice 4 : Système de commandes e-commerce (Pydantic)

Créer un système de commandes avec des modèles imbriqués, `@model_validator`, et la sérialisation/désérialisation :

```python
--8<-- "src/exercices/cours-3-class-et-dataclass/exercice_04_pydantic_ecommerce.py"
```
