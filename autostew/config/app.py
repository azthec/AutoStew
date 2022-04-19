from typing import Set
from typedconfig import Config, key, section

from config.configprovider import provider

USE_CASES = ["Merge", "MergeClose"]


def split_str_set(s: str) -> Set[str]:
    return [x.strip() for x in s.split(",")]


@section('app')
class AppConfig(Config):
    clean_slate = key(cast=bool, default='true', required=False)
    repos_dir = key(cast=str, default='.repos', required=False)
    use_case = key(cast=str)
    projects = key(cast=split_str_set)  # filter which projects to work on
    repos = key(cast=split_str_set)  # filter which repos to work on
    # filter which branches to work on, by username or branch_prefix, this is mandatory as a safety net
    username = key(cast=str)
    branch_prefix = key(cast=str)

    def post_read_hook(self) -> dict:
        config_updates = dict()
        assert self.use_case in USE_CASES
        assert self.username.strip() or self.branch_prefix.strip()
        return config_updates


app_config = AppConfig(provider=provider)
