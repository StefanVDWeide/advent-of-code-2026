from enum import StrEnum
from time import perf_counter
from typing import Annotated, Any

import typer

from advent_of_code_2026.days.abc import Day
from advent_of_code_2026.days.day01.solve import Day01
from advent_of_code_2026.days.day02.solve import Day02
from advent_of_code_2026.days.day03.solve import Day03
from advent_of_code_2026.days.day04.solve import Day04
from advent_of_code_2026.days.day05.solve import Day05
from advent_of_code_2026.days.day06.solve import Day06
from advent_of_code_2026.days.day07.solve import Day07
from advent_of_code_2026.days.day08.solve import Day08
from advent_of_code_2026.days.day09.solve import Day09
from advent_of_code_2026.days.day10.solve import Day10
from advent_of_code_2026.days.day11.solve import Day11
from advent_of_code_2026.days.day12.solve import Day12

DAYS: dict[int, type[Day[Any]]] = {
    1: Day01,
    2: Day02,
    3: Day03,
    4: Day04,
    5: Day05,
    6: Day06,
    7: Day07,
    8: Day08,
    9: Day09,
    10: Day10,
    11: Day11,
    12: Day12,
}


class Part(StrEnum):
    part_1 = "part_1"
    part_2 = "part_2"


# Show the help text if no argument is given
app = typer.Typer(no_args_is_help=True)


@app.command()
def run(
    day: Annotated[
        int | None,
        typer.Argument(
            min=1,
            max=len(DAYS),
            help="Day to run as a number. Runs all days if omitted.",
        ),
    ] = None,
    part: Annotated[
        Part | None,
        typer.Argument(help="Part to run as part_N. Runs both parts if omitted."),
    ] = None,
) -> None:
    """Run the solutions for all days, a single day, or a single part."""

    days = [day] if day is not None else sorted(DAYS)
    parts = [part] if part is not None else list(Part)
    run_all = day is None

    for day_number in days:
        typer.echo(f"Day {day_number:02}")
        day_class = DAYS[day_number]

        try:
            solution = day_class(day_class.input_path())
        except FileNotFoundError:
            typer.echo("no input")
            continue

        # Keeping this broad to no block all days when one raises
        except Exception as error:
            if not run_all:
                raise
            typer.echo(f"error while parsing: {error!r}")
            continue

        for current_part in parts:
            # Clean up the input so that part_1 becomes Part 1
            label = current_part.value.replace("_", " ").capitalize()

            # Also nice to know the solution performance
            start = perf_counter()
            try:
                # Get the part_N function and execute it.
                answer = getattr(solution, current_part.value)()

            except NotImplementedError:
                typer.echo(f"{label}: not solved yet")
                continue

            # Again broad, same reason as above
            except Exception as error:
                if not run_all:
                    raise
                typer.echo(f"{label}: error {error!r}")
                continue

            elapsed_ms = (perf_counter() - start) * 1000

            typer.echo(f"  {label}: {answer} ({elapsed_ms:.2f} ms)")


if __name__ == "__main__":
    app()
