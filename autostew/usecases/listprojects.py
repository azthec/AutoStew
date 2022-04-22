from clients.vcs_server import VCSServer
from config.app import AppConfig


def run(app_config: AppConfig, bitbucket: VCSServer):
    print()
    print("Projects")
    print(" " * 4, end="")
    project_names = (o["name"] for o in bitbucket.project_list())
    print(*project_names, sep=", ")
    print()
