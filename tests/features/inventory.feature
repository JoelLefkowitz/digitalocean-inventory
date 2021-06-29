Feature: Inventory
    
    Scenario: Listing an inventory
        Given I have a digitalocean project
        When I run digitalocean-inventory --list
        Then A json object is dumped to stdout
        And The dumped object implements the inventory schema

    Scenario: Fetching a host
        Given I have a digitalocean project
        When I run digitalocean-inventory --host ...
        Then A json object is dumped to stdout
