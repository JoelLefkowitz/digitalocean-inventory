from dataclasses import dataclass
from typing import Any, Dict

from .exceptions import MissingHostError
from .manager import Manager


@dataclass
class Inventory:
    manager: Manager

    @property
    def inventory(self) -> Dict[str, Any]:
        inventory = {
            "meta": self.manager.meta_hostvars,
            "all": {"hosts": [], "vars": {}, "children": {}},
        }

        for droplet in self.manager.project_droplets:
            ipv4 = self.manager.droplet_ipv4(droplet)
            inventory["all"]["hosts"].append(ipv4)

            if droplet.tags:
                for tag in droplet.tags:
                    if tag in inventory:
                        inventory[tag]["hosts"].append(ipv4)
                    else:
                        inventory[tag] = {"hosts": [ipv4]}

        return inventory

    @property
    def ips(self) -> str:
        return ",".join(
            self.manager.droplet_ipv4(droplet)
            for droplet in self.manager.project_droplets
        )

    # TODO fix host filter
    def host(self, host: str) -> Dict[str, Any]:
        try:
            return self.manager.droplet_hostvars(
                next(
                    filter(
                        lambda x: self.manager.droplet_ipv4(x) is None,
                        self.manager.project_droplets,
                    )
                )
            )

        except StopIteration as err:
            raise MissingHostError(host) from err
