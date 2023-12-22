"""
Delete all .ipynb_checkpoints and __pycache__ folders from given directory.

Use 'recursive' to recursively follow subsequent directories.
"""
from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter
from pathlib import Path
from shutil import rmtree


def clear_jupyter(
    directory: str, recursive: bool = False, verbose: bool = False
) -> None:
    """
    Delete all .ipynb_checkpoints folders from given directory.

    Use 'recursive' to recursively follow subsequent directories.
    """

    path = Path(directory)
    if recursive:
        files = path.rglob(".ipynb_checkpoints")
    else:
        files = path.glob(".ipynb_checkpoints")

    for file in files:
        if verbose:
            print(f"Deleting: {file}")
        rmtree(file)


def clear_pycache(
    directory: str, recursive: bool = False, verbose: bool = False
) -> None:
    """
    Delete all __pycache__ folders from given directory.

    Use 'recursive' to recursively follow subsequent directories.
    """

    path = Path(directory)
    if recursive:
        files = path.rglob("__pycache__")
    else:
        files = path.glob("__pycache__")

    for file in files:
        if verbose:
            print(f"Deleting: {file}")
        rmtree(file)


def clear_hidden(
    directory: str, recursive: bool = False, verbose: bool = False
) -> None:
    clear_jupyter(directory, recursive=recursive, verbose=verbose)
    clear_pycache(directory, recursive=recursive, verbose=verbose)


def parse_args() -> Namespace:
    parser = ArgumentParser(
        description=__doc__,
        formatter_class=RawDescriptionHelpFormatter,
    )

    parser.add_argument("directory")
    parser.add_argument(
        "-r", "--recursive", default=False, action="store_true"
    )
    parser.add_argument("-v", "--verbose", default=False, action="store_true")

    return parser.parse_args()


def main(args: Namespace):
    clear_hidden(
        args.directory, recursive=args.recursive, verbose=args.verbose
    )


def cli():
    main(parse_args())


if __name__ == "__main__":
    main(parse_args())
