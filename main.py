from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Literal
from annotated_types import Gt


class Fruit(BaseModel):
    name: str
    color: Literal['red', 'green']
    weight: Annotated[float, Gt(0)]
    bazam: dict[str, list[tuple[int, bool, float]]]


print(
    Fruit(
        name='Apple',
        color='red',
        weight=4.2,
        bazam={'foobar': [(1, True, 0.1)]},
    )
)


class FruitTwo(BaseModel):
    name: str = Field(max_length=10)
    color: Literal['red', 'green'] = Field(max_length=5)
    weight: Annotated[float, Gt(0)]
    bazam: dict[str, list[tuple[int, bool, float]]]
    email_user: EmailStr
    price: int = Field(ge=0, le=300)


test_dict = {
    "name": 'Apple',
    "color": 'red',
    "weight": 4.2,
    "bazam": {'foobar': [(1, True, 0.1)]},
    "email_user": "example@admin.com",
    "price": 300
}

print(
    FruitTwo(**test_dict)
)
