from pytest_bdd import then


@then("A json object is dumped to stdout")
def a_json_object_is_dumped_to_stdout() -> None:
    pass


@then("The dumped object implements the inventory schema")
def the_dumped_object_implements_the_inventory_schema() -> None:
    pass


@then("The dumped object's hosts are grouped by their tags")
def the_dumped_objects_hosts_are_grouped_by_their_tags() -> None:
    pass


@then("The dumped object has the matched SSH keys in its metadata hostvars")
def the_dumped_object_has_the_matched_ssh_keys_in_its_metadata_hostvars() -> None:
    pass


@then("The dumped object has the SSH key in its metadata hostvars")
def the_dumped_object_has_the_ssh_key_in_its_metadata_hostvars() -> None:
    pass
