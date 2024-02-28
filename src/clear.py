from argparse import ArgumentParser
from winclear import clear

parser = ArgumentParser(description='Flush the Windows command line.')
parser.add_argument('-f',
                    '--force',
                    action='store_true',
                    help='force the command ignoring platform recognition')


def main() -> None:
    args = parser.parse_args()
    clear(force=args.force)
