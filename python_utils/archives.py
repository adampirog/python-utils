import subprocess
import tarfile
from os import getcwd
from pathlib import Path
from shutil import which
from typing import Optional


def extract_archive(
    source_file: str, destination_dir: Optional[str] = None
) -> None:
    """
    Extracts tar archive to a given folder.
    """

    if not destination_dir:
        destination_dir = Path(source_file).with_suffix("")

    with tarfile.open(source_file) as tar:
        tar.extractall(destination_dir)


def create_archive(
    source_dir: str, destination_file: Optional[str] = None
) -> None:
    """
    Creates tar archive from a given folder.

    If possible, uses C-based os tar, as it is much faster than Python
    """

    source_dir = Path(source_dir)
    if which("tar"):
        files = [file.name for file in source_dir.glob("*")]

        if not destination_file:
            destination_file = source_dir.parent / f"{source_dir.name}.tgz"
        else:
            destination_file = Path(getcwd()) / destination_file
        destination_file = destination_file.resolve()

        subprocess.run(
            ["tar", "czf", str(destination_file)] + files,
            cwd=str(source_dir),
            check=True,
        )
    else:
        if not destination_file:
            destination_file = str(source_dir) + ".tgz"

        with tarfile.open(destination_file, "w:gz") as tar:
            for file in source_dir.glob("*"):
                tar.add(file, arcname=file.name)
