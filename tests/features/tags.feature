Feature: Tags
    
    Scenario: Listing a tagged inventory
        Given I have a digitalocean project
        And The project's droplets have tags
        When I run digitalocean-inventory --list
        Then A json object is dumped to stdout
        And The dumped object implements the inventory schema
        And The dumped object's hosts are grouped by their tags
