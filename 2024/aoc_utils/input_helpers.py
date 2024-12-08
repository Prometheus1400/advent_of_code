import os
from enum import Enum
from pathlib import Path


class Input(Enum):
    SAMPLE = "sample"
    INPUT = "input"


def initialize_day(day: int) -> None:
    input_path = Path(os.getcwd()) / "inputs"
    sample_file = input_path / f"{Input.SAMPLE.value}_{day}.txt"
    input_file = input_path / f"{Input.INPUT.value}_{day}.txt"

    if not sample_file.exists():
        sample_file.touch()
    if not input_file.exists():
        input_file.touch()


def get_lines(day: int, kind: Input = Input.INPUT) -> list[str]:
    input_path = Path(os.getcwd()) / "inputs"
    file_path = None
    match kind:
        case Input.SAMPLE:
            file_path = input_path / f"{Input.SAMPLE.value}_{day}.txt"
        case Input.INPUT:
            file_path = input_path / f"{Input.INPUT.value}_{day}.txt"
    assert file_path != None
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def get_text(day: int, kind: Input = Input.INPUT) -> str:
    input_path = Path(os.getcwd()) / "inputs"
    file_path = None
    match kind:
        case Input.SAMPLE:
            file_path = input_path / f"{Input.SAMPLE.value}_{day}.txt"
        case Input.INPUT:
            file_path = input_path / f"{Input.INPUT.value}_{day}.txt"
    assert file_path != None
    with open(file_path, "r") as f:
        return f.read().strip()
