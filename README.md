# DigitalOcean inventory

An ansible dynamic inventory for DigitalOcean

### Status

| Source     | Shields                                                        |
| ---------- | -------------------------------------------------------------- |
| Project    | ![license][license] ![release][release]                        |
| Raised     | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

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


### Docs

Additional details are available in the [Documentation][documentation].

### Tests

Install dependencies:

```bash
pip install .[tests]
```

Run with pytest

```bash
pytest
```

### Versioning

[SemVer](http://semver.org/) is used for versioning. For a list of versions available, see the tags on this repository.

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

Releases are made on every major change.

### Author

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joel_lefkowitz]

See also the list of contributors who participated in this project.

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

None yet!

<!--- Table links --->

[license]: https://img.shields.io/github/license/joellefkowitz/digitalocean-inventory
[release]: https://img.shields.io/github/v/tag/joellefkowitz/digitalocean-inventory
[issues]: https://img.shields.io/github/issues/joellefkowitz/digitalocean-inventory "Issues"
[issues_link]: https://github.com/JoelLefkowitz/digitalocean-inventory/issues
[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/digitalocean-inventory "Pull requests"
[pulls_link]: https://github.com/JoelLefkowitz/digitalocean-inventory/pulls
[documentation]: https://digitalocean-inventory.readthedocs.io/en/latest/
[joel_lefkowitz]: https://github.com/JoelLefkowitz