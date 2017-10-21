#!/usr/bin/env python3
import argparse
import glob
from os.path import pardir, join, abspath
from bin.get_all_aliases import get_all_aliases


def parent(path):
    """Return parent dir."""
    return abspath(join(path, pardir))


RICE_BASE = parent(__file__)
RICE_BIN = join(RICE_BASE, 'bin')

parser = argparse.ArgumentParser(
    description='Show all the rice commands.'
)

rice_bin_commands = glob.glob(f'{RICE_BIN}/*')


# parser.add_argument(
#     'integers',
#     metavar='N',
#     type=int,
#     nargs='+',
#     help='an integer for the accumulator',
# )
# parser.add_argument(
#     '--sum',
#     dest='accumulate',
#     action='store_const',
#     const=sum, default=max,
#     help='sum the integers (default: find the max)',
# )


def main():
    parser.parse_args()
    get_all_aliases()
    for cmd in rice_bin_commands:
        print(cmd)


if __name__ == '__main__':
    main()
