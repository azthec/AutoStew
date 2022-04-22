from typing import List, Optional
from models.repo import Repo
from models.project import Project
from models.pullrequest import PullRequest

class VCSServer:

    def project_list(self) -> List[Project]:
        pass

    def repo_list(self, project_name: str) -> List[Repo]:
        pass

    # TODO: add proper typing and models
    def get_branches(self, repoKey: str, repoName: str, filter: Optional[str]):
        pass
    
    def get_pull_requests(self, project_key, repository_slug) -> List[PullRequest]:
        pass
