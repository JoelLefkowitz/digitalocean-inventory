from fake_module import FakeModule
from pytest_bdd import given

from src.external.fakes import fake_manager_factory


@given("I have a digitalocean project")
def i_have_a_digitalocean_project() -> None:
    fake = FakeModule("digitalocean")
    fake.purge()
    fake.Manager = fake_manager_factory(
        "Fake project", ["1.1.1.1", "2.2.2.2", "3.3.3.3"]
    )


@given("The project's droplets have tags")
def the_projects_droplets_have_tags() -> None:
    pass
