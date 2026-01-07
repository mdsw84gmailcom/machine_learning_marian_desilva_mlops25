from constants import DATA_PATH
import json
from pprint import pprint
from pydantic import BaseModel, Field


# convenience/utility function to read a json file
def read_json(filename):
    with open(DATA_PATH / filename) as file:
        data = json.load(file)

    return data


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    description: str


class Library(BaseModel):
    name: str
    books: list[Book]


pprint(read_json("library.json"))
