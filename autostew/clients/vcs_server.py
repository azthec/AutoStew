from typing import List
from models.repo import Repo
from models.project import Project

class VCSServer:

    def project_list(self) -> List[Project]:
        pass

    def repo_list(self, project_name: str) -> List[Repo]:
        pass