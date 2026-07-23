from dataclasses import dataclass, field
from enum import StrEnum


class Department(StrEnum):
    ADMIN = "admin"
    ACADEMIC = "academic"


@dataclass(kw_only=True, order=True)
class Employee:
    id: int
    name: str
    email: str
    salary: int = field(repr=False)
    department: Department = Department.ADMIN
    project: list[tuple[str, int]] = field(default_factory=list)


if __name__ == "__main__":
    employee1 = Employee(
        id=1,
        name="Aman",
        email="aman@appperfect.com",
        salary=900000,
        department=Department.ACADEMIC,
        project=[("Nvidia", 1), ("Apple", 4)],
    )
    print(employee1)
