from typedconfig import Config, key, section

from config.configprovider import provider


@section('bitbucket')
class BitbucketConfig(Config):
    url = key(cast=str)
    username = key(cast=str)
    password = key(cast=str)
    token = key(cast=str)

    def post_read_hook(self) -> dict:
        config_updates = dict()
        assert self.url.strip()
        assert self.username.strip()
        assert (self.password and self.password.strip()) or (self.token and self.token.strip())
        return config_updates


bitbucket_config = BitbucketConfig(provider=provider)
