# pylint: disable=too-few-public-methods

from typing import Any, Dict, List

from typing_extensions import Protocol


class Droplet(Protocol):
    id: int
    name: str
    networks: Dict[str, Any]


class Project(Protocol):
    id: int
    name: str

    def get_all_resources(self) -> List[str]:
        ...


class Manager(Protocol):
    def get_all_projects(self) -> List[Project]:
        ...

    def get_all_droplets(self) -> List[Droplet]:
        ...


def droplet_ip(droplet: Droplet) -> str:
    network = next(filter(lambda x: x["type"] == "public", droplet.networks["v4"]))
    return network["ip_address"]
