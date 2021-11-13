from enum import Enum
from typing import TypedDict


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


class FoodRating(Enum):
    BAD = 1
    OKAY = 2
    GOOD = 3
    EXCELLENT = 4


class FoodItem(TypedDict):
    name: str
    category: str
    spiceLevel: int


def main() -> None:
    spaghettiRating: FoodRating = FoodRating.EXCELLENT

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

    bestFoodItem: FoodItem = {
            'name': 'spaghetti',
            'category': 'italian',
            'spiceLevel': 1
        }
    prettyGoodFoodItem: FoodItem = {
            'name': 'tom yum',
            'category': 'thai',
            'spiceLevel': 2
        }
    crowdPleaserFoodItem: FoodItem = {
            'name': 'wings',
            'category': 'american',
            'spiceLevel': 10
        }
    foodItems: list[FoodItem] = [
            bestFoodItem,
            prettyGoodFoodItem,
            crowdPleaserFoodItem
        ]

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

    match spaghettiRating:
        case FoodRating.EXCELLENT:
            print("I couldn't agree more!")
        case _:
            print("Get out!")

    for f in foodItems:
        category = f['category']
        name = f['name']
        match f:
            case {'name': 'spaghetti'}:
                print(f'This is the best food! And its category is {category}')
            case _:
                print(f'{name} just isn\'t as good as spaghetti!')


if __name__ == '__main__':
    main()
