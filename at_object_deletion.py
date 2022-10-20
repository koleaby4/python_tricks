from weakref import finalize
from dataclasses import dataclass


@dataclass
class Car:
    make: str
    year: int


def del_handler(make: str, year: int):
    print(f"Your {year} {make} is gone...")


if __name__ == "__main__":
    b = Car("BMW", 2018)
    a1 = a2 = Car("Audi", 2021)

    finalize(a1, del_handler, a1.make, a1.year)

    del b
    del a1
    del a2
