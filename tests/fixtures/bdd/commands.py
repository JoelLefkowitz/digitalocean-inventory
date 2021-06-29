from pytest_bdd import when


@when("I run digitalocean-inventory --list")
def i_run_digitalocean_inventory_list() -> None:
    pass


@when("I run digitalocean-inventory --host ...")
def i_run_digitalocean_inventory_host() -> None:
    pass
