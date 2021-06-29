import re
from dataclasses import dataclass
from backports.cached_property import cached_property

from typing import Any, List

from .exceptions import MissingHost, MissingProject
from .interfaces import Droplet, Manager, droplet_ip


@dataclass
class Client:
    manager: Manager
    project_name: str

    @cached_property
    def project_droplets_ids(self) -> List[Any]:
        try:
            project = next(
                filter(
                    lambda x: x.name == self.project_name,
                    self.manager.get_all_projects(),
                )
            )

            pattern = re.compile(r"^do:droplet:(\d+)$")

            matches = [
                pattern.match(i)
                for i in project.get_all_resources()
                if pattern.match(i)
            ]

            # mypy requires this matching to be broken into two steps
            return [i.group(1) for i in matches if i is not None]

        except StopIteration as err:
            raise MissingProject(self.project_name) from err

    @cached_property
    def droplets(self) -> List[Droplet]:
        return [
            i
            for i in self.manager.get_all_droplets()
            if i.id in self.project_droplets_ids
        ]

    def droplet(self, ip: str) -> Droplet:  # pylint: disable=invalid-name
        try:
            return next(filter(lambda x: droplet_ip(x) == ip, self.droplets))
        except StopIteration as err:
            raise MissingHost(ip) from err
