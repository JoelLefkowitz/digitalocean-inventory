import json
import pprint
from dataclasses import dataclass
from typing import Dict, Optional

from .exceptions import MissingHostError
from .manager import Manager


@dataclass
class Inventory:
    lst: bool
    host: Optional[str]
    manager: Manager
    debug: bool

    def __str__(self) -> str:
        if self.host:
            return self.dump(self.specific_host(self.host))

        elif self.lst:
            return self.dump(self.full_inventory)

        else:
            return self.raw

    @property
    def raw(self) -> str:
        return ",".join(
            self.manager.droplet_ipv4(droplet)
            for droplet in self.manager.project_droplets
        )

    @property
    def full_inventory(self) -> Dict:
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

    def specific_host(self, host: str) -> Dict:
        try:
            host = next(
                filter(
                    lambda x: self.manager.droplet_ipv4(x) == self.host,
                    self.manager.project_droplets,
                )
            )
            return self.manager.droplet_hostvars(host)

        except StopIteration:
            raise MissingHostError(host)

    def dump(self, output: Dict) -> str:
        return pprint.pformat(output, indent=2) if self.debug else json.dumps(output)
