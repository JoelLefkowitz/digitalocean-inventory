# DigitalOcean inventory

An Ansible dynamic inventory for DigitalOcean.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/digitalocean-inventory/review.yml)
![Version](https://img.shields.io/pypi/v/digitalocean-inventory)
![Downloads](https://img.shields.io/pypi/dw/digitalocean-inventory)
![Quality](https://img.shields.io/codacy/grade/5d5c3600cd99457e8d9a3bc3f16adff8)
![Coverage](https://img.shields.io/codacy/coverage/5d5c3600cd99457e8d9a3bc3f16adff8)

## Installation

```bash
pip install digitalocean-inventory
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/digitalocean-inventory).

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

The packages exposes the executable:

```bash
digitalocean-inventory --list
```

Tags and inventory metadata are compiled into the output:

```json
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
    "hosts": ["123.123.123.123"],
    "vars": {},
    "children": {}
  },
  "production": {
    "hosts": ["123.123.123.123"]
  },
  "manager": {
    "hosts": ["123.123.123.123"]
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

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
