#!/usr/bin/env python
from safe_environ import from_env  # type: ignore

from .models.formatter import Formatter
from .models.inventory import Inventory
from .models.manager import Manager
from .services.cli import cli_parser


def fetch(project: str, env: str, ssh_dir: str, stdout: bool = True) -> None:
    args = cli_parser().parse_args()
    formatter = Formatter(env, project, ssh_dir)

    manager = Manager(
        token=from_env("DO_ACCESS_TOKEN"),
        private_ips=args.private_ips,
        formatter=formatter,
    )

    Inventory(manager)


if __name__ == "__main__":
    pass
