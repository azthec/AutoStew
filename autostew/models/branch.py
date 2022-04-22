from typing import List, TypedDict
from models.user import User

class Branch(TypedDict):
    id: str
    name: str # displayId
    author: User
