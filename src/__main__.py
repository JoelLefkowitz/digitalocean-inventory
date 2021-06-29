#!/usr/bin/env python
import json
import sys
from typing import Optional

from digitalocean import Manager

from .exceptions import MissingAccessToken, MissingProjectName
from .external.client import Client
from .models.inventory import Inventory
from .services.cli import cli_parser
from .services.environ import env_parser
from .utils.defaults import default


def fetch(
    access_token: Optional[str] = None,
    project_name: Optional[str] = None,
) -> None:

    env = env_parser()
    cli = cli_parser()

    client = Client(
        Manager(token=default(access_token, env.access_token, MissingAccessToken)),
        default(project_name, env.project_name, MissingProjectName),
    )

    inventory = Inventory(client)

    json.dump(
        inventory.full
        if cli.list
        else inventory.host(cli.host)
        if cli.host
        else inventory.ips,
        sys.stdout,
    )


if __name__ == "__main__":
    fetch(project_name="arcade production")
