# isort: skip_file
# autoflake: skip_file
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

from pytest_bdd import scenario

from .fixtures.bdd.commands import *  # noqa
from .fixtures.bdd.digitalocean import *  # noqa
from .fixtures.bdd.validation import *  # noqa
from .fixtures.bdd.ssh_keys import *  # noqa


@scenario("features/inventory.feature", "Listing an inventory")
def test_listing_an_inventory() -> None:
    pass


@scenario("features/inventory.feature", "Fetching a host")
def test_fetching_a_host() -> None:
    pass


@scenario("features/ssh_keys.feature", "Setting an SSH key")
def test_setting_an_ssh_key() -> None:
    pass


@scenario("features/ssh_keys.feature", "Setting SSH keys from a directory")
def test_setting_ssh_keys_from_a_directory() -> None:
    pass


@scenario("features/tags.feature", "Listing a tagged inventory")
def test_listing_a_tagged_inventory() -> None:
    pass
