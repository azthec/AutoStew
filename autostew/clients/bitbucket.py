from typing import List
from atlassian import Bitbucket
from models.repo import Repo
from models.project import Project
from clients.vcs_server import VCSServer


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
