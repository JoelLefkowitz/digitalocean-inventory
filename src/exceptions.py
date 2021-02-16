class DropletNameError(Exception):
    def __init__(self, name: str, pattern: str) -> None:
        msg = "The droplet's name doesn't match expected the format"
        super().__init__(f"{msg}\nFormat: {pattern}\nName: {name}")


class MissingHostError(Exception):
    def __init__(self, host: str) -> None:
        super().__init__(f"Could not find host with ip: {host}")


class MissingProjectError(Exception):
    def __init__(self, project: str) -> None:
        super().__init__(f"Could not find project with name: {project}")
