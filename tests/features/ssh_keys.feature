Feature: SSH keys
    
    Scenario: Setting an SSH key
        Given I have a digitalocean project
        And I set an SSH key path
        And An SSH key exists at that path
        When I run digitalocean-inventory --list
        Then A json object is dumped to stdout
        And The dumped object has the SSH key in its metadata hostvars

    Scenario: Setting SSH keys from a directory
        Given I have a digitalocean project
        And I set an SSH key directory
        And SSH keys exist in that directory matching the project's droplet's names
        When I run digitalocean-inventory --list
        Then A json object is dumped to stdout
        And The dumped object has the matched SSH keys in its metadata hostvars
