# play with pattern matching and type hints
class Person:
    favorite_food: str
    name: str
    age: int

    def __init__(self, favorite_food: str, name: str, age: int) -> None:
        # self.favorite_food = age # will cause pyright
        # to flag it as a type error
        self.favorite_food = favorite_food
        self.name = name
        self.age = age


def main() -> None:
    youngPerson: Person = Person(
        favorite_food='spaghetti',
        name='Fred',
        age=13)
    grownPerson: Person = Person(
        favorite_food='spaghetti',
        name='Johnny',
        age=46)
    another: Person = Person(
        favorite_food='pizza',
        name='Al',
        age=30)
    people: list[Person] = [youngPerson, grownPerson, another]

    for p in people:
        match p:
            case Person(favorite_food='spaghetti') if p.age > 25:
                print(f'{p.name} is a grown person and likes spaghetti!')
            case Person(favorite_food='spaghetti') if p.age <= 25:
                print(f'{p.name} is young person and likes spaghetti!')
            case _:
                print((
                    f'{p.name} does not like spaghetti, '
                    f'they like {p.favorite_food}'))


if __name__ == '__main__':
    main()
