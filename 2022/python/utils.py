from pathlib import Path


def get_input_path(day: int) -> Path:
    return Path(__file__).parent.parent / "input" / f"input{day:02}.txt"
