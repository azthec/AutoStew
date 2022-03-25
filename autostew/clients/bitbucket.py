from atlassian import Bitbucket


def from_password(url: str, username: str, password: str):
    """Get Bitbucket client using userpass authentication"""
    return Bitbucket(url=url, username=username, password=password)


def from_token(url: str, username: str, token: str):
    """Get Bitbucket client access token authentication"""
    return Bitbucket(url=url, username=username, token=token)
