from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class Employee(BaseModel):
    name: str
    role: str = "Developer"
    address: Address
    skills: list[str] = Field(default_factory=list)


def main() -> None:
    # Pydantic gère nativement les modèles imbriqués
    employee = Employee(
        name="Alice",
        role="Senior Developer",
        address=Address(street="123 Main St", city="Paris", zip_code="75001"),
        skills=["Python", "FastAPI"],
    )
    print(employee)

    # Sérialisation en dictionnaire
    employee_dict = employee.model_dump()
    print(employee_dict)

    # Sérialisation en JSON
    employee_json = employee.model_dump_json(indent=2)
    print(employee_json)

    # Désérialisation depuis un dictionnaire (utile pour les APIs)
    data = {
        "name": "Bob",
        "address": {"street": "456 Rue de Rivoli", "city": "Paris", "zip_code": "75004"},
        "skills": ["SQL", "Terraform"],
    }
    employee_from_dict = Employee.model_validate(data)
    print(employee_from_dict)

    # Désérialisation depuis du JSON
    json_str = '{"name": "Charlie", "address": {"street": "789 Avenue", "city": "Lyon", "zip_code": "69001"}}'
    employee_from_json = Employee.model_validate_json(json_str)
    print(employee_from_json)


if __name__ == "__main__":
    main()
