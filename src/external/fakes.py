# pylint: disable=invalid-name

from dataclasses import dataclass
from random import randint
from string import ascii_lowercase
from typing import Any, Dict, List


from ..utils.strings import randstr


@dataclass
class FakeDroplet:
    ip: str

    id: int = randint(0, 1000)  # nosec
    name: str = randstr(ascii_lowercase, 10)

    @property
    def networks(self) -> Dict[str, Any]:
        return {
            "v4": [
                {
                    "ip_address": self.ip,
                    "netmask": "255.255.255.0",
                    "gateway": "0.0.0.0",  # nosec
                    "type": "public",
                },
            ]
        }


@dataclass
class FakeProject:
    droplets: List[FakeDroplet]

    id: int = randint(0, 1000)  # nosec
    name: str = randstr(ascii_lowercase, 10)

    def get_all_resources(self) -> List[str]:
        return [f"do:droplet:{droplet.id}" for droplet in self.droplets]


def fake_manager_factory(project_name: str, droplet_ips: List[str]) -> Any:
    fake_droplets = [FakeDroplet(ip) for ip in droplet_ips]

    @dataclass
    class FakeManager:
        token: str

        def get_all_projects(self) -> List[FakeProject]:  # pylint: disable=no-self-use
            return [FakeProject(name=project_name, droplets=fake_droplets)]

        def get_all_droplets(self) -> List[FakeDroplet]:  # pylint: disable=no-self-use
            return fake_droplets

    return FakeManager
