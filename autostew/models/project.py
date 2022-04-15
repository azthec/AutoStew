from typing import List
from models.linkself import LinkSelf

class Links:
    self: List[LinkSelf]

class Project:
    key: str
    id: int
    name: str
    public: bool
    type: str
    links: Links
