from typing import Any

from advent_of_code_2026.days.abc import Day


class Day02(Day[str]):
    def parse_data(self, raw_data: str) -> str:
        return raw_data

    def part_1(self) -> Any:
        raise NotImplementedError

    def part_2(self) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    Day02(Day02.input_path()).solve_both_parts()
