from functools import cached_property
from typing import Dict, List

import digitalocean  # type: ignore

from .exceptions import MissingProjectError
from .formatter import Formatter


class Manager:
    def __init__(self, private_ips: bool, formatter: Formatter, token: str) -> None:
        self.private_ips = private_ips
        self.formatter = formatter
        self.manager = digitalocean.Manager(token=token)

    @cached_property
    def project_droplets(self) -> List[digitalocean.Droplet]:
        try:
            project = next(
                filter(
                    lambda x: x.name == self.formatter.project_name,
                    self.manager.get_all_projects(),
                )
            )
        except StopIteration:
            raise MissingProjectError(self.formatter.project_name)

        project_droplet_ids = list(
            map(
                lambda x: int(x.split(":")[2]),
                filter(
                    lambda x: x.split(":")[1] == "droplet", project.get_all_resources()
                ),
            )
        )

        return list(
            filter(
                lambda x: x.id in project_droplet_ids, self.manager.get_all_droplets()
            )
        )

    @property
    def meta_hostvars(self) -> Dict:
        return {
            "hostvars": {
                self.droplet_ipv4(droplet): self.droplet_hostvars(droplet)
                for droplet in self.project_droplets
            }
        }

    def droplet_hostvars(self, droplet: digitalocean.Droplet) -> Dict:
        return {
            "ansible_python_interpreter": "/usr/bin/python3",
            "ansible_ssh_extra_args": "-o StrictHostKeyChecking=no",
            "ansible_ssh_private_key_file": self.formatter.ssh_key_path(
                self.formatter.parse_index(droplet.name)
            ),
        }

    def droplet_ipv4(self, droplet: digitalocean.Droplet) -> str:
        network_tag = "private" if self.private_ips else "public"
        network = next(
            filter(lambda x: x["type"] == network_tag, droplet.networks["v4"])
        )
        return network["ip_address"]
