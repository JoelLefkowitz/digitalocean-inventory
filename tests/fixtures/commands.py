# pylint: disable=invalid-name

from pytest_bdd import when
from simple_pipes import pipe_call


@when("I run digitalocean-inventory --list")
def i_run_digitalocean_inventory_list() -> None:
    pipe_call("digitalocean-inventory --list")


@when("I run digitalocean-inventory --host ...")
def i_run_digitalocean_inventory_host(ip: str = "1.1.1.1") -> None:
    pipe_call(f"digitalocean-inventory --host {ip}")
