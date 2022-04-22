from clients.vcs_server import VCSServer
from config.app import AppConfig
from git import Repo


def run(app_config: AppConfig, bitbucket: VCSServer):
    for repo in (repo for project in app_config.projects for repo in bitbucket.repo_list(project) if repo['name'] in app_config.repos):
        hrefs = repo['links']['clone']
        httpHref = next(href['href'] for href in hrefs if href['name'] == 'http')

        repo_name = repo['name']
        # Repo.clone_from(httpHref, f'./.repos/{repo_name}')

        for branch in bitbucket.get_branches(repo['project']['key'], repo['name'], app_config.branch_prefix):
            # force recheck for author or branch prefix
            if app_config.branch_prefix and app_config.branch_prefix.strip():
                pass
            if app_config.username and app_config.username.strip():
                pass
            print(branch)
