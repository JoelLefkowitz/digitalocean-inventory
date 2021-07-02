#!/usr/bin/env python
import json
import sys
from typing import Any, Dict, Optional  # pylint: disable=unused-import

from digitalocean import Manager

from .exceptions import MissingAccessToken, MissingProjectName
from .models.client import Client
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

    token = default(access_token, env.access_token, MissingAccessToken)
    project = default(project_name, env.project_name, MissingProjectName)

    client = Client(Manager(token=token), project)
    inventory = Inventory(client)

    if cli.list:
        out = inventory.full  # type: str | Dict[str, Any]

    elif cli.host:
        out = inventory.host(cli.host)

    else:
        out = inventory.ips

    json.dump(out, sys.stdout)


if __name__ == "__main__":
    fetch(project_name="Fake")
