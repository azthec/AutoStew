from typing import List, Optional
from clients.vcs_server import VCSServer
from atlassian import Bitbucket
from models.repo import Repo
from models.project import Project
from models.pullrequest import PullRequest


class BitBucket(VCSServer):
    def __init__(self, bitbucket: Bitbucket):
        self.bitbucket = bitbucket

    @classmethod
    def from_password(cls, url: str, username: str, password: str) -> 'BitBucket':
        """Get Bitbucket client using userpass authentication"""
        return cls(Bitbucket(url=url, username=username, password=password))

    @classmethod
    def from_token(cls, url: str, username: str, token: str) -> 'BitBucket':
        """Get Bitbucket client access token authentication"""
        return cls(Bitbucket(url=url, username=username, token=token))

    def project_list(self) -> List[Project]:
        return list(self.bitbucket.project_list())
    
    def repo_list(self, project_name: str) -> List[Repo]:
        return list(self.bitbucket.repo_list(project_name))

    # TODO: add proper typing and models
    def get_branches(self, repo_key: str, repo_name: str, filter: Optional[str] = None):
        return list(self.bitbucket.get_branches(repo_key, repo_name, filter=filter))
    
    def get_pull_requests(self, project_key: str, repository_slug: str) -> List[PullRequest]:
        return [
            PullRequest(id=pr["id"],
                        title=pr["title"],
                        open=pr["open"],
                        merge_outcome=pr["properties"]["mergeResult"]["outcome"],
                        merge_current=pr["properties"]["mergeResult"]["current"],
                        from_branch_id=pr["fromRef"]["id"],
                        from_branch_name=pr["fromRef"]["displayId"],
                        to_branch_id=pr["toRef"]["id"],
                        to_branch_name=pr["toRef"]["displayId"],
                        author=pr["author"]["user"])
            for pr in self.bitbucket.get_pull_requests(project_key, repository_slug)
        ]
        
