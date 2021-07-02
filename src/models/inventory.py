from dataclasses import dataclass
from typing import Any, Dict

from ..external.interfaces import Droplet, droplet_ip
from .client import Client


@dataclass
class Inventory:
    client: Client

    @property
    def ips(self) -> str:
        return ",".join(droplet_ip(droplet) for droplet in self.client.droplets)

    @property
    def full(self) -> Dict[str, Any]:
        return {
            "meta": {
                "hostvars": {
                    droplet_ip(droplet): self.hostvars(droplet)
                    for droplet in self.client.droplets
                }
            },
            "all": {
                "hosts": [droplet_ip(droplet) for droplet in self.client.droplets],
                "vars": {},
                "children": {},
            },
        }

    def host(self, ip: str) -> Dict[str, Any]:  # pylint: disable=invalid-name
        return self.hostvars(self.client.droplet(ip))

    def hostvars(self, droplet: Droplet) -> Dict[str, Any]:
        print(self, droplet)
        return {}
