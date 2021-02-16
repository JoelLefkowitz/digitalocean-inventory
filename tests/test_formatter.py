import pytest
import os
from digitalocean_inventory.formatter import Formatter
from digitalocean_inventory.exceptions import DropletNameError


@pytest.fixture()
def formatter():
    return Formatter(
        project="project",
        env="env",
        ssh_dir="ssh_dir",
    )


def test_project_name(formatter):
    assert formatter.project_name == "project env"


def test_droplet_name(formatter):
    assert formatter.droplet_name(0) == "project-env-0"


def test_ssh_key_path(formatter):
    assert formatter.ssh_key_path(0) == os.path.join("ssh_dir", "project-env-0")


def test_parse_index(formatter):
    assert formatter.parse_index("project-env-0") == 0
    assert formatter.parse_index("project-env-10") == 10

    with pytest.raises(DropletNameError):
        formatter.parse_index("project-en-0")

    with pytest.raises(DropletNameError):
        formatter.parse_index("project-env-")

    with pytest.raises(DropletNameError):
        formatter.parse_index("project-env-a")
