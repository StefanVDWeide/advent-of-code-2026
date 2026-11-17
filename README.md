# advent-of-code-2026

## Project structure

```
.
├── pyproject.toml
├── .python-version
└── src/
    └── advent_of_code_2026/
        ├── cli.py
        └── days/
            ├── abc.py           # Abstract `Day` base class shared by all days
            ├── day01/
            │   ├── solve.py     # Solution for day 1
            │   └── input.txt    # The puzzle input
            ├── day02/
            │   └── ...
            └── day12/
```

- **`days/abc.py`** defines the generic `Day[T]` base class. It reads the puzzle input, strips trailing newlines and passes the text to `parse_data`. The parsed result is stored on `self.puzzle_input`. `Day.input_path()` returns the path of the `input.txt` next to the day's `solve.py`.
- **`days/dayNN/`** contains one folder per day (`day01` … `day12`). Each has a `solve.py` with a `DayNN` class that subclasses `Day`. Every day starts as a stub whose parts raise `NotImplementedError`.
- **`cli.py`** imports every day into the `DAYS` registry and exposes the `run` command.

### The `Day` base class

Each day implements three methods:

| Method                       | Purpose                                                        |
| ---------------------------- | -------------------------------------------------------------- |
| `parse_data(self, raw_data)` | Turn the raw input text into whatever type `T` is most useful. |
| `part_1(self)`               | Return the answer for part 1.                                  |
| `part_2(self)`               | Return the answer for part 2.                                  |

## Usage

Install the dependencies:

```sh
uv sync
```

Then run solutions with the `run` command:

```sh
uv run advent-of-code-2026 run              # all days
uv run advent-of-code-2026 run 5            # both parts of day 5
uv run advent-of-code-2026 run 5 part_1     # only part 1 of day 5
```

Days without an `input.txt` are reported as `no input`, and parts that still raise `NotImplementedError` are reported as `not solved yet`. When running all days, errors in one day are printed and the remaining days still run. When running a single day, errors raise with a full traceback.

## Solving a day

1. Save your puzzle input as `src/advent_of_code_2026/days/dayNN/input.txt`.
2. Fill in `parse_data`, `part_1` and `part_2` in that day's `solve.py`, and change the type parameter to match your parsed input.
3. Run `uv run advent-of-code-2026 run NN`.

### Example

Say the puzzle input is a list of numbers, one per line, and part 1 asks for their sum and part 2 for the largest one:

```python
# src/advent_of_code_2026/days/day01/solve.py
from advent_of_code_2026.days.abc import Day


class Day01(Day[list[int]]):
    def parse_data(self, raw_data: str) -> list[int]:
        return [int(line) for line in raw_data.splitlines()]

    def part_1(self) -> int:
        return sum(self.puzzle_input)

    def part_2(self) -> int:
        return max(self.puzzle_input)


if __name__ == "__main__":
    Day01(Day01.input_path()).solve_both_parts()
```

With an `input.txt` containing:

```
1
2
3
```

Running `uv run advent-of-code-2026 run 1` prints:

```
Day 01
  Part 1: 6 (0.01 ms)
  Part 2: 3 (0.00 ms)
```
