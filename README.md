# DigitalOcean inventory

An Ansible dynamic inventory for DigitalOcean.

## Status

| Source     | Shields                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Project    | ![release][release_shield] ![license][license_shield] ![dependents][dependents_shield]                             |
| Health     | ![travis][travis_shield] ![codacy][codacy_shield] ![coverage][coverage_shield] ![readthedocs][readthedocs_shield]  |
| Repository | ![issues][issues_shield] ![pulls][pulls_shield]                                                                    |
| Publishers | ![pypi][pypi_shield] ![python_versions][python_versions_shield] ![pypi_downloads][pypi_downloads_shield]           |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield] |

## Installation

```bash
pip install digitalocean_inventory
```

## Usage

Export the project environment variables:

```bash
export DO_PROJECT=example
export DO_ENV=production
export DO_SSH_DIR=/Users/joel/.ssh/example
```

Export an access token:

```bash
export DO_ACCESS_TOKEN=<token>
```

The pacakges exposes the executable:

```bash
digitalocean-inventory --list
```

Tags and inventory metadata are compiled into the output:

```bash
{
  "meta": {
    "hostvars": {
      "123.123.123.123": {
        "ansible_python_interpreter": "/usr/bin/python3",
        "ansible_ssh_extra_args": "-o StrictHostKeyChecking=no",
        "ansible_ssh_private_key_file": "/Users/joel/.ssh/example/example-production-0"
      }
    }
  },
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
  "manager": {
    "hosts": [
      "123.123.123.123"
    ]
  }
}
```

The executable has support for host, list and debug flags:

```bash
usage: Digital ocean inventory [-h] [--host [HOST]] [--list [LIST]] [--debug [DEBUG]]
                               [--private-ips [PRIVATE_IPS]]

optional arguments:
  --host [HOST]
  --list [LIST]
  --debug [DEBUG]
  --private-ips [PRIVATE_IPS]
```

To use with the ansible-playbook cli:

**`inventory.py`**:

```python
#!/usr/bin/env python

from digitalocean_inventory import fetch

if __name__ == '__main__':
    fetch()
```

```bash
ansible-playbook -i inventory.py <playbook>
```

You can consume the inventory in order to mutate it before outputting:

```python
#!/usr/bin/env python

from digitalocean_inventory import fetch

if __name__ == '__main__':
    inventory = fetch(stdout=False)
    print(inventory)
```

## Tests

To run unit tests:

```bash
grunt tests:unit
```

To generate a coverage report:

```bash
grunt tests:coverage
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To generate the sphinx configuration:

```bash
grunt docs:generate
```

Then build the documentation:

```bash
grunt docs:build
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

Before commiting new code:

```bash
grunt precommit
```

This will run linters, formaters, generate a test coverage report and the sphinx configuration.

## Versioning

This repository adheres to semantic versioning standards.
For more inforamtion on semantic versioning visit [SemVer][semver].

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

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joellefkowitz]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Github links -->

[pulls]: https://github.com/JoelLefkowitz/digitalocean-inventory/pulls
[issues]: https://github.com/JoelLefkowitz/digitalocean-inventory/issues

<!-- External links -->

[readthedocs]: https://digitalocean-inventory.readthedocs.io/en/latest/
[semver]: http://semver.org/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[joellefkowitz]: https://github.com/JoelLefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/digitalocean-inventory
[license_shield]: https://img.shields.io/github/license/joellefkowitz/digitalocean-inventory
[dependents_shield]: https://img.shields.io/librariesio/dependent-repos/pypi/digitalocean_inventory

<!-- Health shields -->

[travis_shield]: https://img.shields.io/travis/joellefkowitz/digitalocean-inventory
[codacy_shield]: https://img.shields.io/codacy/coverage/digitalocean-inventory
[coverage_shield]: https://img.shields.io/codacy/grade/digitalocean-inventory
[readthedocs_shield]: https://img.shields.io/readthedocs/digitalocean-inventory

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/digitalocean-inventory
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/digitalocean-inventory

<!-- Publishers shields -->

[pypi_shield]: https://img.shields.io/pypi/v/digitalocean_inventory
[python_versions_shield]: https://img.shields.io/pypi/pyversions/digitalocean_inventory
[pypi_downloads_shield]: https://img.shields.io/pypi/dw/digitalocean_inventory

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/digitalocean-inventory
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/digitalocean-inventory
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/digitalocean-inventory
