from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, order=True)
class Person:
    id: int
    name: str
    age: int = 18
    email: str = ""


if __name__ == "__main__":
    person1 = Person(id=1, name="aman", age=24, email="amanbhargava.ab08@gmail.com")
    person2 = Person(id=1, name="aman", age=24, email="amanbhargava.ab08@gmail.com")
    person3 = Person(id=2, name="Akshat", age=24, email="akshatpareek.ap07@gmail.com")

    print(person1)

    print(person1.__dict__)

    print(person1 == person2)
    print(person1 == person3)

    print(person1 > person3)
