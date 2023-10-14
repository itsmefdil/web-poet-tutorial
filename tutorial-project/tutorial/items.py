from attrs import define


@define
class Book:
    title: str
    price: float
    description: str
