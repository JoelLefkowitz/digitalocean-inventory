from random import choices


def randstr(alphabet: str, length: int) -> str:
    return "".join(choices(alphabet, k=length))
