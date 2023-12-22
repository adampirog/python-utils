import importlib
from pathlib import Path
from types import ModuleType


def import_module(python_file: str) -> ModuleType:
    """
    Dynamically import given python file as module.
    """
    python_file = Path(python_file)
    spec = importlib.util.spec_from_file_location(
        python_file.stem, python_file
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
