import os
from typing import Optional

from .exceptions import EmptySSHSelector, MissingSSHKey, SSHDirMatchError


def select_key(
    host_name: str, ssh_key: Optional[str] = None, ssh_dir: Optional[str] = None
) -> str:
    if ssh_key is not None:
        path = ssh_key

    elif ssh_dir is not None:
        if host_name in os.listdir(ssh_dir):
            path = os.path.join(ssh_dir, host_name)
        else:
            raise SSHDirMatchError(host_name, ssh_dir)

    else:
        raise EmptySSHSelector()

    if not os.path.exists(path) or not os.path.isfile(path):
        raise MissingSSHKey(path)

    return os.path.normpath(path)
