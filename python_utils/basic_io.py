import json


def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as handle:
        result = json.load(handle)
    return result


def save_json(data: dict, path: str) -> None:
    with open(path, "wt", encoding="utf-8") as handle:
        json.dump(data, handle)


def load_txt(path: str) -> list:
    with open(path, encoding="utf-8") as handle:
        result = [line.strip() for line in handle]
    return result


def save_txt(data: list, path: str) -> None:
    with open(path, "wt", encoding="utf-8") as handle:
        for line in data:
            handle.write(f"{line}\n")
