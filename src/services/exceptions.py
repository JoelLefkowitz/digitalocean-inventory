class EmptySSHSelector(Exception):
    def __init__(self) -> None:
        super().__init__("The SSH selector didn't have an ssh_key or ssh_dir set.")


class MissingSSHKey(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Could not find an ssh key with the path {path}.")


class SSHDirMatchError(Exception):
    def __init__(self, host_name: str, ssh_dir: str) -> None:
        super().__init__(
            f"""
            Could not find an ssh key matching the name {host_name} in the
            directory {ssh_dir}.
            """
        )
