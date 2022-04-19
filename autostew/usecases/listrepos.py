from clients.vcs_server import VCSServer
from config.app import AppConfig


def run(app_config: AppConfig, bitbucket: VCSServer):
    print()
    for project in app_config.projects:
        print(project)
        print(" " * 4, end="")
        repo_names = (o["name"] for o in bitbucket.repo_list(project))
        print(*repo_names, sep=", ")
        print()
