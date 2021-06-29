import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Environment:
    access_token: Optional[str]
    project_name: Optional[str]
    ssh_key: Optional[str]
    ssh_dir: Optional[str]


def env_parser() -> Environment:
    return Environment(
        access_token=os.environ.get("DO_ACCESS_TOKEN", None),
        project_name=os.environ.get("DO_PROJECT", None),
        ssh_key=os.environ.get("DO_SSH_KEY", None),
        ssh_dir=os.environ.get("DO_SSH_DIR", None),
    )
