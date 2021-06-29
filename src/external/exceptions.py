class MissingProject(Exception):
    def __init__(self, project_name: str) -> None:
        super().__init__(f"Could not find project with name: {project_name}.")


class MissingHost(Exception):
    def __init__(self, ip: str) -> None:
        super().__init__(f"Could not find a host with ip: {ip}.")
