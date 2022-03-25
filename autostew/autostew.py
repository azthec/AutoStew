from clients.bitbucket import from_token
from config.app import app_config
from config.bitbucket import bitbucket_config
from usecases import listrepos, listprojects


def main():
    print(app_config)
    print(bitbucket_config)
    bitbucket = from_token(bitbucket_config.url, bitbucket_config.username, bitbucket_config.token)
    # print(*bitbucket.project_list(), sep=", ")
    # print(*bitbucket.repo_list(app_config.projects[0]), sep=", ")
    listprojects.run(app_config, bitbucket)
    listrepos.run(app_config, bitbucket)


if __name__ == "__main__":
    main()
