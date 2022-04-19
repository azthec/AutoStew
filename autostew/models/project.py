from typing import List, TypedDict
from models.linkself import LinkSelf

class Links(TypedDict):
    self: List[LinkSelf]

class Project(TypedDict):
    key: str
    id: int
    name: str
    public: bool
    type: str
    links: Links
