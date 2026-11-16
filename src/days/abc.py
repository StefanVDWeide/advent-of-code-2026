from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Day[T](ABC):
    puzzle_input: T

    def __init__(self, puzzle_input_path: Path) -> None:
        self.puzzle_input = self.parse_data(path=puzzle_input_path)

    @abstractmethod
    def parse_data(self, path: Path) -> T: ...

    @abstractmethod
    def part_1(self) -> Any: ...

    @abstractmethod
    def part_2(self) -> Any: ...

    def solve_both_parts(self) -> None:
        print(f"The solution for day 1 is: {self.part_1()}")
        print(f"The solution for day 2 is: {self.part_2()}")
