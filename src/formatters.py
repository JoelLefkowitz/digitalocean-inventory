import os
import re
from dataclasses import dataclass
from exceptions import DropletNameError


@dataclass
class Formatter:
    project: str
    env: str
    ssh_dir: str

    @property
    def project_name(self) -> str:
        return f"{self.project} {self.env}"

    def droplet_name(self, index) -> str:
        return f"{self.project}-{self.env}-{index}"

    def ssh_key_path(self, index) -> str:
        return os.path.join(self.ssh_dir, f"{self.project}-{self.env}-{index}")

    def parse_index(self, name) -> str:
        prefix = f"^{self.project}-{self.env}-"
        suffix = "[0-9]*.$"
        pattern = prefix + suffix

        if not re.match(pattern, name):
            raise DropletNameError(name, pattern)

        return re.search(suffix, name).group()
