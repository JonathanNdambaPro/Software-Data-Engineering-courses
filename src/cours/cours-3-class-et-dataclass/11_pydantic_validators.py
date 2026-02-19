from pydantic import BaseModel, field_validator, model_validator


class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Le nom du produit ne peut pas être vide")
        return v.strip().title()

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Le prix doit être positif")
        return round(v, 2)

    @model_validator(mode="after")
    def check_stock_value(self) -> "Product":
        """Validation qui dépend de plusieurs champs à la fois."""
        if self.price * self.quantity > 1_000_000:
            raise ValueError("La valeur totale du stock ne peut pas dépasser 1 000 000")
        return self


def main() -> None:
    # Le field_validator transforme le nom automatiquement
    product = Product(name="  laptop  ", price=999.999, quantity=10)
    print(product)  # name='Laptop', price=1000.0

    # model_validator vérifie la combinaison prix * quantité
    try:
        Product(name="Expensive Item", price=10000, quantity=200)
    except Exception as e:
        print(f"Erreur : {e}")

    # field_validator rejette un nom vide
    try:
        Product(name="   ", price=10, quantity=1)
    except Exception as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
