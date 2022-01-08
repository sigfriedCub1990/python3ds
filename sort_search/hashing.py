#!/bin/python


def hash_str(a_string: str, table_size: int) -> int:
    return sum([ord(c) for c in a_string]) % table_size


def has_str_positional(a_string: str, table_size: int) -> int:
    return (
        sum([ord(c) * i for c in a_string for i in range(1, len(a_string))])
        % table_size
    )


if __name__ == "__main__":
    print(hash_str("ruben", 11))
    print(has_str_positional("ruben", 11))
    print(has_str_positional("nebur", 11))
