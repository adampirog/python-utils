from pathlib import Path

from python_utils.archives import create_archive, extract_archive


def test_archive_creation(tmpdir):
    root_dir = Path(tmpdir.mkdir("test"))
    folder = root_dir / "folder"
    folder.mkdir(exist_ok=True, parents=True)

    for i in range(10):
        file = folder / f"file_{i}.txt"
        file.touch()

    target = root_dir / "target.tgz"
    create_archive(folder, target)
    assert target.is_file()


def test_archive_creation_defaukt_target(tmpdir):
    root_dir = Path(tmpdir.mkdir("test"))
    folder = root_dir / "folder"
    folder.mkdir(exist_ok=True, parents=True)

    for i in range(10):
        file = folder / f"file_{i}.txt"
        file.touch()

    target = folder.with_suffix(".tgz")
    create_archive(folder)
    assert target.is_file()


def test_archive_extraction(tmpdir):
    root_dir = Path(tmpdir.mkdir("test"))
    folder = root_dir / "folder"
    folder.mkdir(exist_ok=True, parents=True)

    for i in range(10):
        file = folder / f"file_{i}.txt"
        file.touch()

    target = root_dir / "target.tgz"
    create_archive(folder, target)
    assert target.is_file()

    restore = root_dir / "restore"

    extract_archive(target, restore)
    assert restore.is_dir()

    for index, file in enumerate(sorted(restore.glob("*"))):
        assert file.name == f"file_{index}.txt"


def test_archive_extraction_default_target(tmpdir):
    root_dir = Path(tmpdir.mkdir("test"))
    folder = root_dir / "folder"
    folder.mkdir(exist_ok=True, parents=True)

    for i in range(10):
        file = folder / f"file_{i}.txt"
        file.touch()

    target = root_dir / "target.tgz"
    create_archive(folder, target)
    assert target.is_file()

    restore = root_dir / "target"

    extract_archive(target)
    assert restore.is_dir()

    for index, file in enumerate(sorted(restore.glob("*"))):
        assert file.name == f"file_{index}.txt"
