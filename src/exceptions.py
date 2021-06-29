class MissingAccessToken(Exception):
    def __init__(self) -> None:
        super().__init__("No DigitalOcean access token name was set")


class MissingProjectName(Exception):
    def __init__(self) -> None:
        super().__init__("No project name was set")
