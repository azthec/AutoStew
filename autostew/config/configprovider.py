from typedconfig.provider import ConfigProvider
from typedconfig.source import EnvironmentConfigSource, IniFileConfigSource

provider = ConfigProvider()
provider.add_source(EnvironmentConfigSource(prefix="AUTOSTEW"))
provider.add_source(IniFileConfigSource("config.ini"))

__all__ = ["provider"]