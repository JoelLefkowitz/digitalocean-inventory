from argparse import ArgumentParser


def cli_parser() -> ArgumentParser:
    parser = ArgumentParser("Digital ocean inventory")
    parser.add_argument("--host", type=str, nargs="?", default=False)
    parser.add_argument("--list", type=bool, nargs="?", default=False, const=True)
    parser.add_argument(
        "--private-ips", type=bool, nargs="?", default=False, const=True
    )
    return parser
