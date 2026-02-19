from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=150)
    email: str


def main() -> None:
    # Pydantic valide automatiquement les types et les contraintes
    user = User(name="Alice", age=30, email="alice@example.com")
    print(user)

    # Pydantic convertit automatiquement les types compatibles (coercion)
    user_coerced = User(name="Bob", age="25", email="bob@example.com")  # "25" -> 25
    print(user_coerced)
    print(type(user_coerced.age))  # <class 'int'>

    # Validation échouée : age négatif
    try:
        User(name="Charlie", age=-5, email="charlie@example.com")
    except Exception as e:
        print(f"Erreur de validation : {e}")

    # Validation échouée : nom trop court
    try:
        User(name="A", age=30, email="a@example.com")
    except Exception as e:
        print(f"Erreur de validation : {e}")


if __name__ == "__main__":
    main()
