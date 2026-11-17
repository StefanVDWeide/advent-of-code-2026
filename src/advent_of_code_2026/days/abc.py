import inspect
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Day[T](ABC):
    puzzle_input: T

    def __init__(self, puzzle_input_path: Path) -> None:
        raw_data = puzzle_input_path.read_text().strip("\n")
        self.puzzle_input = self.parse_data(raw_data)

    @classmethod
    def input_path(cls, filename: str = "input.txt") -> Path:
        return Path(inspect.getfile(cls)).parent / filename

    @abstractmethod
    def parse_data(self, raw_data: str) -> T: ...

    @abstractmethod
    def part_1(self) -> Any: ...

    @abstractmethod
    def part_2(self) -> Any: ...

    def solve_both_parts(self) -> None:
        print(f"The solution for part 1 is: {self.part_1()}")
        print(f"The solution for part 2 is: {self.part_2()}")
