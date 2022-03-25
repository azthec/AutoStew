from atlassian import Bitbucket
from config.app import AppConfig


def run(app_config: AppConfig, bitbucket: Bitbucket):
    print()
    print("Projects")
    print(" " * 4, end="")
    repo_names = (o["name"] for o in bitbucket.project_list())
    print(*repo_names, sep=", ")
    print()