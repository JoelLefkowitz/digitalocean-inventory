# DigitalOcean inventory

An Ansible dynamic inventory for DigitalOcean.

## Status

| Source     | Shields                                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Project    | ![release][release_shield] ![license][license_shield] ![lines][lines_shield] ![languages][languages_shield]                     |
| Health     | ![codacy][codacy_shield] ![readthedocs][readthedocs_shield] ![travis][travis_shield] ![codacy_coverage][codacy_coverage_shield] |
| Repository | ![issues][issues_shield] ![issues_closed][issues_closed_shield] ![pulls][pulls_shield] ![pulls_closed][pulls_closed_shield]     |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]                        |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield]              |

## Installing

```bash
pip install digitalocean-inventory
```

## Usage

Set an access token and the project name as environment variables. The digitalocean-inventory executable acts as an [inventory script][inventory_scripts] for all droplets in the project:

```bash
export DO_PROJECT=example
export DO_ACCESS_TOKEN=...

$ digitalocean-inventory

123.123.123.123
```

```bash
$ digitalocean-inventory --list

{
    "all": {
    "hosts": [
        "123.123.123.123"
    ],
    "vars": {},
    "children": {}
    }
}
```

```bash
$ digitalocean-inventory --host 123.123.123.123

{}
```

## Features

### Extensibility

You can extend the behavior of the inventory by importing it as a python package:

```python
import json
import sys

from digitalocean_inventory import fetch

inventory = fetch(project)
json.dump(inventory.list, sys.stdout)

{
    "all": {
    "hosts": [
        "123.123.123.123"
    ],
    "vars": {},
    "children": {}
    }
}
```

```python
json.dump(inventory.host("123.123.123.123"), sys.stdout)

{}
```

### SSH keys

You can set an ssh key to use to communicate with droplets and it will be added to the droplet metadata:

```bash
export DO_SSH_KEY=/Users/joel/.ssh/example

$ digitalocean-inventory --list

{
  "meta": {
    "hostvars": {
      "123.123.123.123": {
        "ansible_ssh_extra_args": "-o StrictHostKeyChecking=no",
        "ansible_ssh_private_key_file": "/Users/joel/.ssh/example"
      }
    }
  },
  "all": {
    "hosts": [
        "123.123.123.123"
    ],
    "vars": {},
    "children": {}
    }
}
```

```bash
$ digitalocean-inventory --host 123.123.123.123

{
    "ansible_ssh_extra_args": "-o StrictHostKeyChecking=no",
    "ansible_ssh_private_key_file": "/Users/joel/.ssh/example"
}
```

You can set an ssh directory instead and droplets will be paired with ssh keys matching their names:

```bash
export DO_SSH_DIR=/Users/joel/.ssh/example

$ digitalocean-inventory --list

{
  "meta": {
    "hostvars": {
      "123.123.123.123": {
        "ansible_ssh_extra_args": "-o StrictHostKeyChecking=no",
        "ansible_ssh_private_key_file": "/Users/joel/.ssh/example/droplet-0"
      }
    }
  },
  "all": {
    "hosts": [
        "123.123.123.123"
    ],
    "vars": {},
    "children": {}
    }
}
```

### Droplet tags

Droplets with tags will be grouped:

```bash
$ digitalocean-inventory --list

  {
    "all": {
    "hosts": [
        "123.123.123.123"
    ],
    "vars": {},
    "children": {}
    },
    "production": {
        "hosts": [
        "123.123.123.123"
        ]
    },
    "managers": {
        "hosts": [
        "123.123.123.123"
        ]
    }
  }
```

## Tests

To run unit tests and generate a coverage report:

```bash
grunt test
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

## Continuous integration

This repository uses github actions to lint and test each commit. Formatting tasks and writing/generating documentation must be done before committing new code.

## Versioning

This repository adheres to semantic versioning standards.
For more information on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][author]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Public links -->

[semver]: http://semver.org/

<!-- External links -->

[readthedocs]: https://digitalOcean-inventory.readthedocs.io/en/latest/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif
[inventory_scripts]: https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html#developing-inventory-scripts

<!-- Acknowledgments -->

[author]: https://github.com/joellefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/digitalOcean-inventory
[license_shield]: https://img.shields.io/github/license/joellefkowitz/digitalOcean-inventory
[lines_shield]: https://img.shields.io/tokei/lines/github/joellefkowitz/digitalOcean-inventory
[languages_shield]: https://img.shields.io/github/languages/count/joellefkowitz/digitalOcean-inventory

<!-- Health shields -->

[codacy_shield]: https://img.shields.io/codacy/grade/5d5c3600cd99457e8d9a3bc3f16adff8
[readthedocs_shield]: https://img.shields.io/readthedocs/digitalOcean-inventory
[travis_shield]: https://img.shields.io/travis/com/joellefkowitz/digitalOcean-inventory
[codacy_coverage_shield]: https://img.shields.io/codacy/coverage/5d5c3600cd99457e8d9a3bc3f16adff8

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/digitalOcean-inventory
[issues_closed_shield]: https://img.shields.io/github/issues-closed/joellefkowitz/digitalOcean-inventory
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/digitalOcean-inventory
[pulls_closed_shield]: https://img.shields.io/github/issues-pr-closed/joellefkowitz/digitalOcean-inventory

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/digitalocean-inventory
[python_versions_shield]: https://img.shields.io/pypi/pyversions/digitalocean-inventory
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/digitalocean-inventory

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/digitalOcean-inventory
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/digitalOcean-inventory
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/digitalOcean-inventory
