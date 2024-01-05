import dataclasses
import json
from datetime import date, datetime, timedelta

import numpy as np


class ExtendedJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if dataclasses.is_dataclass(obj):
            return dataclasses.asdict(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, (np.floating, np.complexfloating)):
            return float(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.string_):
            return str(obj)
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, timedelta):
            return str(obj)
        return super().default(obj)


def save_json(data: dict, path: str) -> None:
    with open(path, "wt", encoding="utf-8") as handle:
        json.dump(data, handle, indent=4, cls=ExtendedJsonEncoder)


def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as handle:
        result = json.load(handle)
    return result


def save_txt(data: list, path: str) -> None:
    with open(path, "wt", encoding="utf-8") as handle:
        for line in data:
            handle.write(f"{line}\n")


def load_txt(path: str) -> list:
    with open(path, encoding="utf-8") as handle:
        result = [line.strip() for line in handle]
    return result
