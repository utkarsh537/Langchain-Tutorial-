from typing import TypedDict
class Person(TypedDict):
    name: str
    age: int
person1: Person = {"name": "utkarsh", "age": 30}
print(person1)