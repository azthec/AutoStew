from os import path
from shutil import rmtree
from clients.bitbucket import BitBucket
from clients.vcs_server import VCSServer
from config.app import app_config
from config.bitbucket import bitbucket_config
from usecases import listprojects, listrepos, merge

def main():
    if app_config.clean_slate and path.exists(app_config.repos_dir) and path.isdir(app_config.repos_dir):
        rmtree(app_config.repos_dir) 
    print(app_config)
    print(bitbucket_config)
    
    bitbucket: VCSServer = BitBucket.from_token(bitbucket_config.url, bitbucket_config.username, bitbucket_config.token)
    print(list(bitbucket.project_list())[0]["name"])
    # print(*bitbucket.project_list(), sep=", ")
    # print(*bitbucket.repo_list(app_config.projects[0]), sep=", ")
    # listprojects.run(app_config, bitbucket)
    listrepos.run(app_config, bitbucket)
    # merge.run(app_config, bitbucket)

if __name__ == "__main__":
    main()
