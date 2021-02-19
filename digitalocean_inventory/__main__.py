#!/usr/bin/env python
import argparse

from safe_environ import from_env  # type: ignore

from .formatter import Formatter
from .inventory import Inventory
from .manager import Manager

parser = argparse.ArgumentParser("Digital ocean inventory")
parser.add_argument("--host", type=str, nargs="?", default=False)
parser.add_argument("--list", type=bool, nargs="?", default=False, const=True)
parser.add_argument("--debug", type=bool, nargs="?", default=False, const=True)
parser.add_argument("--private-ips", type=bool, nargs="?", default=False, const=True)


def fetch(stdout=True) -> Inventory:
    args = parser.parse_args()

    formatter = Formatter(
        project=from_env("DO_PROJECT"),
        env=from_env("DO_ENV"),
        ssh_dir=from_env("DO_SSH_DIR"),
    )

    manager = Manager(
        token=from_env("DO_ACCESS_TOKEN"),
        private_ips=args.private_ips,
        formatter=formatter,
    )

    inventory = Inventory(
        lst=args.list, host=args.host, manager=manager, debug=args.debug
    )

    if stdout:
        print(inventory)

    return inventory


if __name__ == "__main__":
    fetch()