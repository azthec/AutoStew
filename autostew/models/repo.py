from typing import TypedDict, List
from models.project import Project
from models.linkclone import LinkClone
from models.linkself import LinkSelf

class Links(TypedDict):
    clone: List[LinkClone]
    self: List[LinkSelf]

class Repo(TypedDict):
    id: int
    name: str
    state: str
    forkable: bool
    project: Project
    public: bool
    links: Links
