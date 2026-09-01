"""
Delete all .ipynb_checkpoints and __pycache__ folders from given directory.

Use 'recursive' to recursively follow subsequent directories.
"""

from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter
from pathlib import Path
from shutil import rmtree


def clear_tree(
    directory: str | Path, name: str, *, recursive: bool = False, verbose: bool = False
) -> None:
    """
    Delete all the 'name' folders from given directory.

    Use 'recursive' to recursively follow subsequent directories.
    """
    path = Path(directory)
    search_function = path.rglob if recursive else path.glob

    for file in search_function(name):
        if verbose:
            print(f"Deleting: {file}")
        rmtree(file)


def clear_hidden(directory: str, recursive: bool = False, verbose: bool = False) -> None:
    """
    Delete all the '.ipynb_checkpoints' and '__pycache__' folders from given directory.

    Use 'recursive' to recursively follow subsequent directories.
    """
    clear_tree(directory, name=".ipynb_checkpoints", recursive=recursive, verbose=verbose)
    clear_tree(directory, name="__pycache__", recursive=recursive, verbose=verbose)


def parse_args() -> Namespace:
    parser = ArgumentParser(
        description=__doc__,
        formatter_class=RawDescriptionHelpFormatter,
    )

    parser.add_argument("directory")
    parser.add_argument("-r", "--recursive", default=False, action="store_true")
    parser.add_argument("-v", "--verbose", default=False, action="store_true")

    return parser.parse_args()


def main(args: Namespace):
    clear_hidden(args.directory, recursive=args.recursive, verbose=args.verbose)


def cli():
    main(parse_args())


if __name__ == "__main__":
    main(parse_args())
