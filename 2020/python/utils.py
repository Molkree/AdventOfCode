from os import path


def get_input_path(day: int) -> str:
    return path.join(
        path.dirname(path.abspath(__file__)), "..", "input", f"input{day:02}.txt"
    )
