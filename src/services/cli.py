from argparse import ArgumentParser, Namespace


def cli_parser() -> Namespace:
    parser = ArgumentParser("Digital ocean inventory")
    parser.add_argument("--host", type=str, nargs="?", default=None)
    parser.add_argument("--list", type=bool, nargs="?", default=False, const=True)
    return parser.parse_args()
