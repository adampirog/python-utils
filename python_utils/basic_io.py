import dataclasses
import json
from datetime import date, datetime, timedelta

import numpy as np


class ExtendedJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, (np.floating, np.complexfloating)):
            return float(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.string_):
            return str(o)
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        if isinstance(o, timedelta):
            return str(o)
        return super().default(o)


def save_json(data: dict, path: str) -> None:
    with open(path, "wt", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, cls=ExtendedJsonEncoder)


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
