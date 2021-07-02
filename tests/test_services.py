import os

import pytest
from mock_file_tree import FileTree, MockFileTree

from src.services.exceptions import (EmptySSHSelector, MissingSSHKey,
                                     SSHDirMatchError)
from src.services.ssh_keys import select_key


def test_select_key() -> None:
    host_name = "droplet-1"

    with pytest.raises(EmptySSHSelector):
        assert select_key(host_name)

    with MockFileTree(os, FileTree.from_paths("test-key")):
        assert select_key(host_name, ssh_key="test-key") == "test-key"

        with pytest.raises(MissingSSHKey):
            assert select_key(host_name, ssh_key="another-key")

    with MockFileTree(os, FileTree.from_paths("droplet-1")):
        assert select_key(host_name, ssh_dir=".") == "droplet-1"

        with pytest.raises(SSHDirMatchError):
            assert select_key(host_name="droplet-2", ssh_dir=".")
