from argparse import ArgumentParser, Namespace


def cli_parser() -> Namespace:
    parser = ArgumentParser("Digital ocean inventory")
    add_key(parser, "--host")
    add_option(parser, "--list")
    add_option(parser, "--debug")
    return parser.parse_args()


def add_key(parser: ArgumentParser, key: str) -> None:
    parser.add_argument(key, type=str, nargs="?", default=None)


def add_option(parser: ArgumentParser, option: str) -> None:
    parser.add_argument(option, type=bool, nargs="?", default=False, const=True)
