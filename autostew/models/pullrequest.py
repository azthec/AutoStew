from typing import List, TypedDict
from models.user import User

class PullRequest(TypedDict):
    id: str
    title: str
    open: bool

    merge_outcome: str # from properties.mergeResult.outcome one of "CLEAN"
    current: bool     # from properties.mergeResult.current

    # from "fromRef.id" and "fromRef.displayId", TODO: check that type is "BRANCH"
    from_branch_id: str # refs/heads/update/example-dependency-0.0.1
    from_branch_name: str # update/example-dependency-0.0.1

    # from "toRef", TODO: check that type is "BRANCH"
    to_branch_id: str # refs/heads/update/example-dependency-0.0.1
    to_branch_name: str # update/example-dependency-0.0.1

    author: User # from author.user
